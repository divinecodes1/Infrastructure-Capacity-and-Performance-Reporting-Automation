from pathlib import Path


def write_html(path: Path, title: str, body: str) -> Path:
    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{body}</p></body></html>"
    path.write_text(content, encoding="utf-8")
    return path
