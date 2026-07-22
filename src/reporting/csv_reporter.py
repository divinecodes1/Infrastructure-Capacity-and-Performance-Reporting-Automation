import csv
from pathlib import Path


def write_csv(path: Path, rows: list[dict]) -> Path:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys() if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    return path
