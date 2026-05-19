from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from src.mimo_client import MiMoClient
from src.prompt_templates import SYSTEM_PROMPT, TASK_PROMPTS


class StudyMateAgent:
    """Agent pipeline for academic study support."""

    def __init__(self, model: str, temperature: float = 0.3, max_tokens: int = 1800):
        self.client = MiMoClient(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def build_prompt(self, task_type: str, input_text: str, output_language: str) -> str:
        task_instruction = TASK_PROMPTS.get(task_type, TASK_PROMPTS["Full Study Pack"])

        return f"""
Task type: {task_type}
Preferred output language: {output_language}

Agent workflow:
Step 1: Identify the topic and important concepts.
Step 2: Clean and organise the messy input.
Step 3: Explain difficult points in a student-friendly way.
Step 4: Produce the requested output format.
Step 5: Add a short token-use reflection explaining why this task benefits from long-context AI.

Task instruction:
{task_instruction}

Input material:
\"\"\"
{input_text}
\"\"\"
"""

    def run(self, task_type: str, input_text: str, output_language: str) -> Dict[str, Any]:
        user_prompt = self.build_prompt(task_type, input_text, output_language)

        response = self.client.chat(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        )

        return {
            "content": response["content"],
            "metadata": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "task_type": task_type,
                "output_language": output_language,
                "model": response["model"],
                "usage": response["usage"],
                "elapsed_seconds": response["elapsed_seconds"],
                "input_characters": len(input_text),
            }
        }
