import json

from core.huggingface_client import HuggingFaceClient

with open("config.json","r") as f:
    config = json.load(f)

api = config["huggingface"]["api_key"]

client = HuggingFaceClient(api)

print(client.image_caption("assets/image.jpg"))
