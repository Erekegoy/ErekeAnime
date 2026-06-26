import json
from core.gemini_client import GeminiClient

try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    api_key = config["gemini"]["api_key"]

    if not api_key:
        print("❌ Gemini API ключ пустой")
        raise SystemExit

    print("🔄 Проверка Gemini API...")

    client = GeminiClient(api_key)

    result = client.test()

    print("\n===== Ответ Gemini =====")
    print(result)

except Exception as e:
    print("❌ Ошибка:")
    print(e)
