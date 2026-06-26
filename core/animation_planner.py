class AnimationPlanner:

    def build_prompt(self, scene):

        prompt = f"""
Anime cinematic scene.

Scene:
{scene["scene"]}

Characters:
{", ".join(scene["characters"])}

Emotion:
{scene["emotion"]}

Camera:
{scene["camera"]}

Animation:
{scene["animation"]}

Music:
{scene["music"]}

Sound effects:
{", ".join(scene["sfx"])}

Duration:
{scene["duration"]} seconds.

High quality anime.
Smooth animation.
Movie quality.
60 FPS.
"""

        return prompt.strip()
