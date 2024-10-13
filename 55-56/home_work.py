import tkinter as tk
import requests

class GraphicView():
    def __init__(self, bot):
        """Показывает заметки в окне"""
        self._create_window()
        self.bot = bot
        self.root.mainloop()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title('Чат с ботом')

        # окошко для ввода
        self.input = tk.Text(self.root, height=10, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для ввода
        self.input_role = tk.Text(self.root, height=10, width=20)
        self.input_role.grid(row=1, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Text(self.root, height=20, width=100)
        self.output.grid(row=0, column=1, padx=10, pady=10, rowspan=3)


        self.button = tk.Button(self.root, text='Отправить запрос', command=self.send_request)
        self.button.grid(row=2, column=0, padx=10, pady=10)

    def send_request(self):
        text = self.input.get('1.0', tk.END)
        text_role = self.input_role.get('1.0', tk.END)
        response = self.bot.send_request(text, text_role)

        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, response)


class YandexGPT:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog

    def send_request(self, question, role_text):
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        prompt = {
            "modelUri": f'gpt://{self.catalog}/yandexgpt-lite',
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": 200
            },
            "messages": [
                {
                    "role": "system",
                    "text": f"{role_text}"
                },
                {
                    "role": "user",
                    "text": f"{question}"
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, headers=headers, json=prompt)
        text = response.json()['result']['alternatives'][0]['message']['text']
        return text


token = ''
catalog = ''

bot = YandexGPT(token, catalog)
graphic_view = GraphicView(bot)