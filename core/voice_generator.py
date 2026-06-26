class VoiceGenerator:

    def __init__(self):
        self.provider = "future"

    def generate(self, scene):

        print("\n🎙 Voice Generator")

        text = f"""
Narration:
{scene["scene"]}

Emotion:
{scene["emotion"]}
"""

        print(text)

        return text
