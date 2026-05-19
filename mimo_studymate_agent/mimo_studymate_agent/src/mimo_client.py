from __future__ import annotations

import time
from typing import Dict, List, Any

from litellm import completion


class MiMoClient:
    """Small wrapper around LiteLLM Xiaomi MiMo provider."""

    def __init__(self, model: str, temperature: float = 0.3, max_tokens: int = 1800):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def chat(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        started = time.time()

        response = completion(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        elapsed = round(time.time() - started, 2)
        content = response["choices"][0]["message"]["content"]

        usage = getattr(response, "usage", None)
        if usage is None and isinstance(response, dict):
            usage = response.get("usage", {})

        return {
            "content": content,
            "usage": dict(usage) if usage else {},
            "elapsed_seconds": elapsed,
            "model": self.model,
        }
