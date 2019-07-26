import json
from telegram import TelegramBot


class HolaX(TelegramBot):

    def __init__(self):
        self.message_text = None
        self.check = False
        with open('model/action.json') as json_file:
            self.data = json.load(json_file)

    def action(self):
        for x in self.data['actions']:
            if self.text in x:
                self.message_text = x[self.text]
                self.check = True
        if self.check:
            self.message_text = 'Hello {}, good morning'.format(self.text)

        success = self.send_message(self.message_text)
        return success
