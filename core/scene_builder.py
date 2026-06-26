import json
import os


class SceneBuilder:

    def __init__(self):
        os.makedirs("outputs/scenes", exist_ok=True)

    def save(self, panel_name, scene):

        filename = os.path.join(
            "outputs/scenes",
            panel_name + ".json"
        )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                scene,
                f,
                ensure_ascii=False,
                indent=4
            )

        return filename
