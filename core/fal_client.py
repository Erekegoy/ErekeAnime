import requests


class FalClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def test(self):

        url = "https://fal.run/fal-ai/wan-i2v"

        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": "anime",
            "image_url": "https://fal.media/files/panda.jpeg"
        }

        try:
            r = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=60
            )

            return {
                "status": r.status_code,
                "response": r.text
            }

        except Exception as e:
            return {
                "error": str(e)
            }
