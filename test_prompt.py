import json

from core.animation_planner import AnimationPlanner

planner = AnimationPlanner()

with open("outputs/scenes/panel_1.json","r",encoding="utf-8") as f:
    scene=json.load(f)

print(planner.build_prompt(scene))
