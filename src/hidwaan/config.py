from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent.parent

TEMPLATE_DIR = SRC_DIR / "templates"
STATIC_DIR = SRC_DIR / "static"
DB_FILE = ROOT_DIR / "local.db"
