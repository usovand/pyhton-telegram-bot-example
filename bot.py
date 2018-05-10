import asyncio
import aiohttp

from aiohttp import web
from urllib.parse import urljoin

from config.host import *


async def handle_updates(request):
    body = await request.json()
    asyncio.ensure_future(process_updates(body))

    return web.Response()


async def process_updates(updates):
    first_name = updates['message']['chat'].get('first_name')
    chat_id = updates['message']['chat']['id']

    await send_api_request(
        'sendMessage',
        json={
            'chat_id': chat_id,
            'text': 'Hello {}!'.format(first_name)
        }
    )


async def send_api_request(method, json=None):
    if json is None:
        json = {}

    async with aiohttp.ClientSession() as session:
        async with session.post(urljoin(API_URL, method), json=json) as resp:
            return resp


def run_updates_handler():
    app = web.Application()
    app.add_routes([web.post('/' + TOKEN, handle_updates)])

    web.run_app(app)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_api_request('setWebhook', json={'url': WEBHOOK_URL}))

    run_updates_handler()
