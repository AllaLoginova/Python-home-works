import requests


class YandexGPT:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog

    def send_request(self, user_text, leng):
        url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": f"{leng}",
            # "targetLanguageCode": "en",
            "format": "HTML",
            "texts": [
                f"{user_text}"
            ],
            "folderId": f"{self.catalog}",
            "speller": False
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, json=payload, headers=headers)
        text = response.json()['translations'][0]['text']
        return text