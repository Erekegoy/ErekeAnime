import base64
import mimetypes
import requests
import json


class GeminiClient:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            "gemini-2.5-flash:generateContent"
        )

    def analyze_image(self, image_path):

        mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"

        with open(image_path, "rb") as f:
            img = base64.b64encode(f.read()).decode()

        prompt = """
Ты режиссёр аниме.

Верни ТОЛЬКО JSON.

Формат:

{
 "scene":"",
 "characters":[],
 "emotion":"",
 "camera":"",
 "animation":"",
 "music":"",
 "sfx":[],
 "duration":0
}
"""

        body = {
            "contents":[
                {
                    "parts":[
                        {
                            "text":prompt
                        },
                        {
                            "inline_data":{
                                "mime_type":mime,
                                "data":img
                            }
                        }
                    ]
                }
            ]
        }

        r = requests.post(
            self.url,
            params={"key":self.api_key},
            json=body,
            timeout=120
        )

        answer = r.json()

        try:
            text = answer["candidates"][0]["content"]["parts"][0]["text"]

            text = text.replace("```json","")
            text = text.replace("```","").strip()

            return json.loads(text)

        except Exception:

            return answer
