import flask
import requests

from threading import Thread

TOKEN = 'token'
BOT_API_URL = 'https://api.telegram.org/bot' + TOKEN + '/{method}'

WEBHOOK_PORT = 8081
WEBHOOK_URL = '167.99.214.149:' + str(WEBHOOK_PORT) + '/' + TOKEN

SERVER = flask.Flask(__name__)


@SERVER.route('/' + TOKEN, methods=['POST'])
def webhook():
    data = flask.request.get_data().decode('utf-8')
    Thread(target=run, kwargs={'update_data': data}).start()

    return flask.Response(status=200)


def send_api_request(method: str, data=None) -> requests.Response:
    """
    Send request to telegram bot api

    :param method: api method
    :param data: additional data
    :return: api response
    """
    if data is None:
        data = {}

    r = requests.post(BOT_API_URL.format(method=method), json=data)

    return r


def run(update_data):
    print(update_data)


if __name__ == '__main__':
    send_api_request('setWebhook', {'url': WEBHOOK_URL})

    SERVER.run(host='0.0.0.0', port=WEBHOOK_PORT)