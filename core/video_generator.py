import os
import json


class VideoGenerator:

    def __init__(self):

        self.providers = [
            "fal",
            "future"
        ]

    def generate(self, prompt):

        print("\n🎬 Video Generator")

        for provider in self.providers:

            print(f"➡️ Попытка: {provider}")

            if provider == "fal":

                result = self.generate_fal(prompt)

                if result:
                    return result

            if provider == "future":

                break

        print("⚠️ Нет доступного Video AI.")

        return None

    def generate_fal(self, prompt):

        if not os.path.exists("config.json"):
            return None

        with open("config.json","r",encoding="utf-8") as f:

            cfg=json.load(f)

        if "fal" not in cfg:
            return None

        key = cfg["fal"]["api_key"]

        if key == "":
            return None

        print("✅ FAL API найден.")

        print("⏳ Генерация будет подключена позже.")

        return None
