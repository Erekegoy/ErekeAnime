import os


class OCREngine:

    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def extract_text(self, image_path):

        if not os.path.exists(image_path):
            return []

        if not self.enabled:
            print("OCR Engine отключен.")
            return []

        # Пока заглушка.
        # Позже здесь подключим PaddleOCR или облачный OCR.
        return []

    def translate(self, text, target_language="ru"):

        return text
