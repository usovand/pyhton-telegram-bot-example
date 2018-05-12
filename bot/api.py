#!/usr/bin/env python3

from aiohttp import ClientSession, ClientResponse
from urllib.parse import urljoin

from bot.config import API_URL, LOGGER


METHOD_SET_WEBHOOK = 'setWebhook'
METHOD_SEND_MESSAGE = 'sendMessage'


async def send_request(method: str, **kwargs) -> ClientResponse:
    """ Send bot api request """
    LOGGER.info('send request {}'.format(method))
    LOGGER.debug('With {}'.format(kwargs))

    url = urljoin(API_URL, method)

    async with ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            return response
