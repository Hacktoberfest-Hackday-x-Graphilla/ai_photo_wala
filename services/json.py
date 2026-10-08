import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
THEMES_FILE = BASE_DIR / "data" / "themes.json"


def _load_themes():
    with open(THEMES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_themes():
    return _load_themes()["themes"]


def get_theme_by_id(id):
    themes = _load_themes()["themes"]

    for theme in themes:
        if theme.get("id") == id:
            return theme

    return None
