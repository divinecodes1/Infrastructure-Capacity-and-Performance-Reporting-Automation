from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def get_setting(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)
