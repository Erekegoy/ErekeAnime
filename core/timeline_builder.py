import json
import os


class TimelineBuilder:

    def __init__(self):

        self.timeline = []

        os.makedirs("outputs/project", exist_ok=True)

    def add_scene(
        self,
        scene,
        video=None,
        voice=None,
        music=None
    ):

        self.timeline.append({

            "scene": scene,

            "video": video,

            "voice": voice,

            "music": music

        })

    def save(self):

        filename = "outputs/project/timeline.json"

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.timeline,
                f,
                ensure_ascii=False,
                indent=4
            )

        print("💾 Timeline сохранён:")
        print(filename)

        return filename
