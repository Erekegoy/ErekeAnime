import json

from core.gemini_client import GeminiClient

with open("config.json","r",encoding="utf-8") as f:
    cfg=json.load(f)

client=GeminiClient(cfg["gemini"]["api_key"])

result=client.analyze_image("assets/image.jpg")

print(result)
