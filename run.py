#!/usr/bin/env python3

import asyncio

from aiohttp import web

from bot.api import *
from bot.config import WEBHOOK_URL, WEBHOOK_ROUTE


async def catch_update(request: web.Request) -> web.Response:
    """ Catch webhook request and run update handler """
    update = await request.json()
    asyncio.ensure_future(handle(update))

    return web.Response()


async def set_webhook() -> None:
    """ Set webhook url """
    async with ClientSession() as session:
        await send_request(
            session,
            METHOD_SET_WEBHOOK,
            json={'url': WEBHOOK_URL}
        )


def run_bot() -> None:
    """ Run bot """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhook())

    server = web.Application()
    server.add_routes(
        [web.post(WEBHOOK_ROUTE, catch_update)]
    )

    web.run_app(server)


async def handle(update: dict) -> None:
    """ Handle update """
    async with ClientSession() as session:
        await send_request(
            session,
            METHOD_SEND_MESSAGE,
            json={
                'chat_id': update['message']['chat']['id'],
                'text': 'Hello my dear friend!',
            }
        )


if __name__ == '__main__':
    run_bot()
