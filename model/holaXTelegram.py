import requests
import json
from model import config
from model.telegram import TelegramBot


class HolaX:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.message_text = None
        self.success = False
        self.check = False
        with open('model/action.json') as json_file:
            self.data = json.load(json_file)

    def set_webhook(self):
        requests.get(config.TELEGRAM_INIT_WEBHOOK_URL)

    def parse_json(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.text = message['text']

    def action(self):
        for x in self.data['actions']:
            if self.text in x:
                self.message_text = x[self.text]
                self.check = True
        if self.check:
            self.message_text = 'Hello {}, good morning'.format(self.text)
        success = self.send_message()
        return success

    def send_message(self):
        res = requests.get(config.TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.message_text))
        return True if res.status_code == 200 else False
