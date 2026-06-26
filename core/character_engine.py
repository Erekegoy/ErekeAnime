import hashlib


class CharacterEngine:

    def __init__(self):
        self.characters = {}

    def register(self, image_path):

        key = hashlib.md5(
            image_path.encode("utf-8")
        ).hexdigest()

        if key not in self.characters:

            self.characters[key] = {
                "image": image_path,
                "name": f"Character_{len(self.characters)+1}",
                "scenes": 1
            }

        else:

            self.characters[key]["scenes"] += 1

        return self.characters[key]

    def get_all(self):
        return self.characters

    def clear(self):
        self.characters.clear()
