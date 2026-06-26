import json
import os


class ProviderManager:

    def __init__(self):

        self.config = {}

        if os.path.exists("config.json"):

            with open(
                "config.json",
                "r",
                encoding="utf-8"
            ) as f:

                self.config = json.load(f)

    def get_video_provider(self):

        if "fal" in self.config:

            key = self.config["fal"].get(
                "api_key",
                ""
            )

            if key:
                return "fal"

        return None

    def get_llm_provider(self):

        if "gemini" in self.config:

            key = self.config["gemini"].get(
                "api_key",
                ""
            )

            if key:
                return "gemini"

        return None

    def status(self):

        return {

            "video": self.get_video_provider(),

            "llm": self.get_llm_provider()

        }
