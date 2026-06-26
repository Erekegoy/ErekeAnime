from datetime import datetime
import os

from core.anime_director import AnimeDirector

APP_NAME = "ErekeAnime Studio"
VERSION = "0.5.0"


def banner():
    print("=" * 60)
    print(f"🎬 {APP_NAME} v{VERSION}")
    print("AI Manga ➜ Anime Studio")
    print("=" * 60)


def check_folders():

    folders = [
        "assets",
        "outputs",
        "models",
        "temp",
        "logs",
        "core",
        "ui"
    ]

    print("\n📂 Проверка проекта:\n")

    for folder in folders:

        if os.path.exists(folder):
            print(f"✅ {folder}")

        else:
            print(f"❌ {folder}")


def main():

    banner()

    print("\n🚀 Запуск ErekeAnime Studio")
    print("🕒", datetime.now())

    check_folders()

    director = AnimeDirector()

    director.start()

    print("\n" + "=" * 60)
    print("✅ ErekeAnime Studio завершил работу.")
    print("=" * 60)


if __name__ == "__main__":
    main()
