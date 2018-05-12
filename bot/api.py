#!/usr/bin/env python3

from aiohttp import ClientSession
from urllib.parse import urljoin

from bot.config import API_URL


METHOD_SET_WEBHOOK = 'setWebhook'
METHOD_SEND_MESSAGE = 'sendMessage'


async def send_request(method, **kwargs):
    """ Send bot api request """
    url = urljoin(API_URL, method)

    async with ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            return response
