import json
import os

from core.gemini_client import GeminiClient
from core.panel_detector import detect_panels
from core.scene_builder import SceneBuilder

with open("config.json","r",encoding="utf-8") as f:
    cfg=json.load(f)

client=GeminiClient(cfg["gemini"]["api_key"])
builder=SceneBuilder()

image="assets/image.jpg"

print("📖 Разделение на панели...")

panels=detect_panels(image)

print(f"Найдено панелей: {len(panels)}")

for i,panel in enumerate(panels,1):

    print(f"\n🧠 Анализ панели {i}")

    scene=client.analyze_image(panel)

    file=builder.save(f"panel_{i}",scene)

    print("✅ Сохранено:",file)

print("\n🎬 Pipeline завершён.")
