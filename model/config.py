LOCAL_WEBHOOK = 'https://heroku-hello-gunicorn.herokuapp.com/{}'.format(endpoint)

TOKEN = '759338335:AAEEm_Nwqx4uX0NIYJIRSrMtr7KCn3i8R8s'

BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)

TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
