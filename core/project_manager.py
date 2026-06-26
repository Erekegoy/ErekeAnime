import json
import os
from datetime import datetime


class ProjectManager:

    def __init__(self):

        self.folder = "outputs/projects"

        os.makedirs(self.folder, exist_ok=True)

    def create(self, name):

        project = {

            "name": name,

            "created": str(datetime.now()),

            "status": "processing",

            "video": "",

            "scenes": []

        }

        filename = os.path.join(
            self.folder,
            f"{name}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                project,
                f,
                ensure_ascii=False,
                indent=4
            )

        return filename

    def update_status(
        self,
        filename,
        status
    ):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            project = json.load(f)

        project["status"] = status

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                project,
                f,
                ensure_ascii=False,
                indent=4
            )

    def set_video(
        self,
        filename,
        video
    ):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            project = json.load(f)

        project["video"] = video

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                project,
                f,
                ensure_ascii=False,
                indent=4
            )
