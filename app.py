from flask import Flask, request, jsonify
from holaXTelegram import HolaX

app = Flask(__name__)
bot = HolaX()
bot.set_webhook()


@app.route('/')
def hello():
    return '<h1>Hello There!</h1>'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.parse_json(req)
    success = bot.action()
    return jsonify(success=success)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
