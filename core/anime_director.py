from datetime import datetime
import json

from core.loader import load_images
from core.panel_detector import detect_panels

from core.gemini_client import GeminiClient
from core.scene_builder import SceneBuilder
from core.video_prompt_builder import VideoPromptBuilder
from core.video_generator import VideoGenerator
from core.voice_generator import VoiceGenerator
from core.music_generator import MusicGenerator
from core.timeline_builder import TimelineBuilder


class AnimeDirector:

    def __init__(self):

        with open("config.json","r",encoding="utf-8") as f:
            cfg=json.load(f)

        self.gemini = GeminiClient(
            cfg["gemini"]["api_key"]
        )

        self.scene_builder = SceneBuilder()
        self.prompt_builder = VideoPromptBuilder()

        self.video = VideoGenerator()
        self.voice = VoiceGenerator()
        self.music = MusicGenerator()

        self.timeline = TimelineBuilder()

    def start(self):

        print("\n🎬 Anime Director")
        print(datetime.now())

        images = load_images()

        print(f"\n📚 Глав найдено: {len(images)}")

        for image in images:

            panels = detect_panels(image)

            print(f"\nПанелей: {len(panels)}")

            for i, panel in enumerate(panels,1):

                print(f"\n🧠 Панель {i}")

                scene = self.gemini.analyze_image(panel)

                self.scene_builder.save(
                    f"panel_{i}",
                    scene
                )

                prompt = self.prompt_builder.build(scene)

                video = self.video.generate(prompt)

                voice = self.voice.generate(scene)

                music = self.music.generate(scene)

                self.timeline.add_scene(
                    scene,
                    video,
                    voice,
                    music
                )

        self.timeline.save()

        print("\n✅ AI Pipeline завершён.")
