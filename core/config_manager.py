import json
import os


class ConfigManager:

    def __init__(self):

        self.path = "config.json"

        self.data = {
            "cloud": {
                "enabled": False,
                "provider": "",
                "api_key": "",
                "base_url": ""
            },
            "video": {
                "fps": 30,
                "resolution": "1080p"
            },
            "audio": {
                "enabled": True
            }
        }

    def load(self):

        if os.path.exists(self.path):

            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)

        return self.data

    def save(self):

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get(self, key):

        return self.data.get(key)

    def set(self, key, value):

        self.data[key] = value
