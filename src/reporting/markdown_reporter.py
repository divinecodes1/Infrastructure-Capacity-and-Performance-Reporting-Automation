from pathlib import Path


def write_markdown(path: Path, title: str, body: str) -> Path:
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")
    return path
