import json
from core.video_prompt_builder import VideoPromptBuilder

with open("outputs/scenes/panel_1.json","r",encoding="utf-8") as f:
    scene=json.load(f)

builder=VideoPromptBuilder()

print(builder.build(scene))
