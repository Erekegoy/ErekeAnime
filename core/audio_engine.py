import os


class AudioEngine:

    def __init__(self):
        self.voices = []
        self.music = None

    def set_music(self, music_path):

        if os.path.exists(music_path):
            self.music = music_path

    def add_voice(self, voice_path):

        if os.path.exists(voice_path):
            self.voices.append(voice_path)

    def get_music(self):
        return self.music

    def get_voices(self):
        return self.voices

    def clear(self):
        self.voices = []
        self.music = None

    def summary(self):

        return {
            "voices": len(self.voices),
            "music": self.music
        }
