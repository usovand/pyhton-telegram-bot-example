#!/usr/bin/env python3

from aiohttp import ClientSession, ClientResponse
from urllib.parse import urljoin

from bot.config import API_URL

METHOD_SET_WEBHOOK = 'setWebhook'
METHOD_SEND_MESSAGE = 'sendMessage'


async def send_request(session: ClientSession, method: str, **kwargs) -> ClientResponse:
    """ Send bot api request """
    url = urljoin(API_URL, method)
    return await session.post(url, **kwargs)
