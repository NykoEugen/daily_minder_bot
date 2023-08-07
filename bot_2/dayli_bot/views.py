from pprint import pprint

import requests
from flask import request

from dayli_bot import app


BOT_TOKEN = '6272568521:AAEXGFm1bmaAvlOubXbWr-zOskrYLE-zNg8'
TG_BASE_URL = 'https://api.telegram.org/bot'


@app.route('/', methods=["POST"])
def greet():
    pprint(request.json)
    chat_id = request.json.get('message').get('chat').get('id')
    data = {
        'chat_id': chat_id,
        'text': 'Hi there!'
    }
    requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)
    return 'Ok', 200
