import os


class SceneManager:

    def __init__(self):
        self.scenes = []

    def add_scene(self, panel_path, video_path):

        scene = {
            "panel": panel_path,
            "video": video_path,
            "duration": 5,
            "effects": [],
            "voice": None,
            "music": None
        }

        self.scenes.append(scene)

    def get_scenes(self):
        return self.scenes

    def clear(self):
        self.scenes = []

    def total(self):
        return len(self.scenes)

    def export(self, output_file="outputs/project.scenes"):

        os.makedirs("outputs", exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as file:

            for scene in self.scenes:

                file.write(f"{scene['panel']}\n")
                file.write(f"{scene['video']}\n")
                file.write(f"{scene['duration']}\n")
                file.write("--------------------\n")

        return output_file
