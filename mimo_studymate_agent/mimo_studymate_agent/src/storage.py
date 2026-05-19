from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any, List

LOG_PATH = Path("data/run_logs.jsonl")


def save_run_log(result: Dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")


def load_recent_logs(limit: int = 5) -> List[Dict[str, Any]]:
    if not LOG_PATH.exists():
        return []

    lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
    recent = lines[-limit:]
    return [json.loads(line) for line in reversed(recent)]
