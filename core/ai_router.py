class AIRouter:

    def __init__(self):
        self.services = {
            "gemini": False,
            "huggingface": False,
            "fal": False
        }

    def enable(self, name):
        if name in self.services:
            self.services[name] = True

    def disable(self, name):
        if name in self.services:
            self.services[name] = False

    def available(self):
        return [k for k, v in self.services.items() if v]

    def route(self, task):

        if task == "video":
            return "fal"

        if task == "ocr":
            return "huggingface"

        if task == "color":
            return "huggingface"

        if task == "story":
            return "gemini"

        if task == "voice":
            return "gemini"

        if task == "music":
            return "gemini"

        return None
