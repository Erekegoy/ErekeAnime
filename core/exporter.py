import os
import json
import shutil


class Exporter:

    def __init__(self):

        self.project = "outputs/project"

        os.makedirs(self.project, exist_ok=True)

    def export(
        self,
        timeline_file,
        final_video=None
    ):

        project = {

            "name": "ErekeAnime Project",

            "version": "0.6",

            "timeline": timeline_file,

            "video": final_video,

            "status": "finished"

        }

        with open(
            os.path.join(
                self.project,
                "project.json"
            ),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                project,
                f,
                ensure_ascii=False,
                indent=4
            )

        if final_video and os.path.exists(final_video):

            shutil.copy(
                final_video,
                os.path.join(
                    self.project,
                    "final_video.mp4"
                )
            )

        print("\n📦 Проект экспортирован.")
        print(self.project)

        return self.project
