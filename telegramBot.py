import requests
import config


class TelegramBot:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.message_text = None
        self.success = False

    def set_webhook(self):
        requests.get(config.TELEGRAM_INIT_WEBHOOK_URL)

    def parse_json(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.text = message['text']

    def action(self):
        if self.text == '/start':
            self.message_text = 'Hello, I am a bot and my owner is Ivan Rodriguez Gomez'.format('creador')
        else:
            self.message_text = 'Hello {}, good morning'.format(self.text)
        success = self.send_message()
        return success

    def send_message(self):
        res = requests.get(config.TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.message_text))
        return True if res.status_code == 200 else False
