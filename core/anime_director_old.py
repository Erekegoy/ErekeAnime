from datetime import datetime

from core.loader import load_images
from core.image_reader import read_image
from core.preprocess import preprocess_image
from core.panel_detector import detect_panels
from core.animator import animate_panel
from core.video_merger import merge_videos

from core.motion_engine import MotionEngine
from core.character_engine import CharacterEngine
from core.scene_manager import SceneManager
from core.audio_engine import AudioEngine
from core.cloud_client import CloudClient
from core.ai_router import AIRouter
from core.ocr_engine import OCREngine
from core.colorizer import Colorizer
from core.config_manager import ConfigManager


class AnimeDirector:

    def __init__(self):
        self.motion = MotionEngine()
        self.characters = CharacterEngine()
        self.scenes = SceneManager()
        self.audio = AudioEngine()
        self.cloud = CloudClient()
        self.router = AIRouter()
        self.ocr = OCREngine()
        self.colorizer = Colorizer()
        self.config = ConfigManager()
        self.videos = []

    def start(self):
        print("\n🎬 Anime Director")
        print(datetime.now())

        self.config.load()

        cloud = self.config.get("cloud")

        if cloud:
            self.cloud.configure(
                cloud.get("base_url", ""),
                cloud.get("api_key", "")
            )

            if self.cloud.is_ready():
                print("☁️ Cloud AI подключен.")
            else:
                print("☁️ Cloud AI не настроен.")

        images = load_images()

        print(f"\n📚 Глав найдено: {len(images)}")

        if len(images) == 0:
            print("Нет изображений.")
            return

        for image in images:
            self.process_image(image)

        self.finish()

    def process_image(self, image):

        info = read_image(image)

        if info is None:
            return

        print("\n==============================")
        print(info["path"])

        preprocess_image(image)

        image = self.colorizer.colorize(image)

        panels = detect_panels(image)

        print(f"Панелей: {len(panels)}")

        for i, panel in enumerate(panels, start=1):

            self.characters.register(panel)

            self.ocr.extract_text(panel)

            output = f"outputs/videos/panel_{i}.mp4"

            if animate_panel(panel, output):
                self.videos.append(output)
                self.scenes.add_scene(panel, output)

    def finish(self):

        if len(self.videos) == 0:
            return

        final = "outputs/videos/final_video.mp4"

        merge_videos(self.videos, final)

        self.scenes.export()

        print("\n🎬 Проект сохранён.")
        print(final)

        print("\n👥 Персонажей:", len(self.characters.get_all()))
        print("🎞 Сцен:", self.scenes.total())
