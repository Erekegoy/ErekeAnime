class VideoPromptBuilder:

    def build(self, scene):

        characters = ", ".join(scene["characters"])
        sfx = ", ".join(scene["sfx"])

        return f"""
masterpiece,
best quality,
anime movie,
cinematic lighting,
ultra detailed,
60 fps,
smooth animation,

Scene:
{scene["scene"]}

Characters:
{characters}

Emotion:
{scene["emotion"]}

Camera:
{scene["camera"]}

Animation:
{scene["animation"]}

Lighting:
Cinematic

Music mood:
{scene["music"]}

Sound effects:
{sfx}

Duration:
{scene["duration"]} seconds

Highly detailed anime.
Professional animation.
Makoto Shinkai movie quality.
Stable camera.
Natural motion.
"""
