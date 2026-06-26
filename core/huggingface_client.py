import requests


class HuggingFaceClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def image_caption(self, image_path):

        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            with open(image_path, "rb") as image:

                response = requests.post(
                    API_URL,
                    headers=headers,
                    data=image,
                    timeout=120
                )

            return response.json()

        except Exception as e:

            return {
                "error": str(e)
            }
