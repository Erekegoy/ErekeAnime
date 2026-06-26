class MusicGenerator:

    def __init__(self):
        self.provider = "future"

    def generate(self, scene):

        print("\n🎵 Music Generator")

        music = {
            "style": scene["music"],
            "duration": scene["duration"]
        }

        print(music)

        return music
