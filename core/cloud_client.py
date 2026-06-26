import requests


class CloudClient:

    def __init__(self):

        self.base_url = ""
        self.api_key = ""

    def configure(self, base_url, api_key):

        self.base_url = base_url
        self.api_key = api_key

    def is_ready(self):

        return (
            self.base_url != ""
            and
            self.api_key != ""
        )

    def animate(self, image_path):

        if not self.is_ready():

            print("☁️ Cloud AI не настроен.")

            return None

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        with open(image_path, "rb") as image:

            response = requests.post(
                self.base_url,
                headers=headers,
                files={
                    "file": image
                },
                timeout=600
            )

        if response.status_code == 200:

            return response.content

        print(response.status_code)

        print(response.text)

        return None
