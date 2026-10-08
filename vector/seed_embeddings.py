import json
from pathlib import Path

from vector.embedding import get_embedding

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "themes.json"


def seed_embeddings():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        themes = json.load(file)

    for theme in themes["themes"]:
        text = f"{theme['name']}. {theme['description']}"
        embedding = get_embedding(text)
        theme["embedding"] = embedding.tolist()

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            themes,
            file,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    seed_embeddings()
