from flask import Flask, request, jsonify
from telegram import TelegramBot

app = Flask(__name__)
bot = TelegramBot()


@app.route('/')
def hello():
    return '<h1>Hola esta es la pagina de Ivan Rodriguez</h1>'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.parse_json(req)
    success = bot.action()
    return jsonify(success=success)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
