from datetime import datetime
import os

from core.loader import load_images
from core.image_reader import read_image
from core.preprocess import preprocess_image
from core.panel_detector import detect_panels
from core.animator import animate_panel
from core.video_merger import merge_videos

APP_NAME = "ErekeAnime"
VERSION = "0.4.0"


def banner():
    print("=" * 50)
    print(f"🎬 {APP_NAME} v{VERSION}")
    print("AI Manga ➜ Anime Generator")
    print("=" * 50)


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

    print("\n📂 Проверка папок:")

    for folder in folders:
        if os.path.exists(folder):
            print(f"✅ {folder}")
        else:
            print(f"❌ {folder}")


def main():
    banner()

    print("\n🚀 Система успешно запущена")
    print("🕒", datetime.now())

    check_folders()

    images = load_images()

    print(f"\n🖼 Найдено изображений: {len(images)}")

    if not images:
        print("⚠️ В папке assets нет изображений.")
        return

    os.makedirs("outputs/videos", exist_ok=True)

    videos = []

    for path in images:

        print("\n" + "=" * 50)

        info = read_image(path)

        if info is None:
            print(f"❌ Не удалось открыть: {path}")
            continue

        print(f"📄 Файл: {info['path']}")
        print(f"📐 Размер: {info['width']} × {info['height']}")

        result = preprocess_image(path)

        if result:
            print(f"💾 Серое изображение сохранено:")
            print(f"   {result}")
        else:
            print("❌ Ошибка обработки")
            continue

        panels = detect_panels(path)

        print(f"\n🧩 Найдено панелей: {len(panels)}")

        if len(panels) == 0:
            print("⚠️ Панели не найдены.")
            continue

        for i, panel in enumerate(panels, start=1):

            print(f"   {i}. {panel}")

            video_path = f"outputs/videos/panel_{i}.mp4"

            success = animate_panel(panel, video_path)

            if success:
                print(f"🎥 Видео сохранено: {video_path}")
                videos.append(video_path)
            else:
                print("❌ Ошибка создания видео.")

    if len(videos) > 0:

        final_video = "outputs/videos/final_video.mp4"

        success = merge_videos(videos, final_video)

        if success:
            print("\n🎬 Финальное видео создано!")
            print(final_video)
        else:
            print("\n❌ Не удалось объединить видео.")

    print("\n" + "=" * 50)
    print("✅ ErekeAnime завершил работу.")
    print("=" * 50)


if __name__ == "__main__":
    main()
