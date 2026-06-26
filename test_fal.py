import json
from core.fal_client import FalClient

try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    api_key = config["fal"]["api_key"]

    if not api_key:
        print("❌ FAL API ключ пустой")
        raise SystemExit

    print("🔄 Проверка fal.ai API...")

    client = FalClient(api_key)

    result = client.test()

    print("\n===== Ответ fal.ai =====")
    print(result)

except Exception as e:
    print("❌ Ошибка:")
    print(e)
