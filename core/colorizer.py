import os


class Colorizer:

    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def colorize(self, image_path):

        if not os.path.exists(image_path):
            return None

        if not self.enabled:
            return image_path

        # Здесь позже подключим AI-раскраску
        return image_path

    def status(self):

        if self.enabled:
            return "AI Colorizer: ON"

        return "AI Colorizer: OFF"
