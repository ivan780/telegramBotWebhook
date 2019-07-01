import requests
from model import config


class TelegramBot:
    def __init__(self):
        self.chat_id = None
        self.text = 'hola'
        self.success = False

    def set_webhook(self):
        requests.get(config.TELEGRAM_INIT_WEBHOOK_URL)

    def parse_json(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.text = message['text']

    def send_message(self, message_text):
        res = requests.get(config.TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, message_text))
        return True if res.status_code == 200 else False
