import json
from pathlib import Path


def write_json(path: Path, payload: dict) -> Path:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    return path
