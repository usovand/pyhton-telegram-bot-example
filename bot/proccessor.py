#!/usr/bin/env python3

from bot.api import *


async def handle_message(message: dict) -> None:
    if message['text'] == '/ReplyKeyboardMarkup':
        await keyboard_markup(message['chat']['id'])
    elif message['text'] == '/Text':
        await text(message['chat']['id'])
    else:
        await text(message['chat']['id'])


async def keyboard_markup(chat_id: int) -> None:
    async with ClientSession() as session:
        await send_request(
            session,
            METHOD_SEND_MESSAGE,
            json={
                'chat_id': chat_id,
                'reply_markup': [
                    [
                        {
                            'text': 'Button1',
                        },
                        {
                            'text': 'Button2',
                        }
                    ],
                    [
                        {
                            'text': 'Button3',
                        },
                        {
                            'text': 'Button4',
                        },
                    ],
                ],
            }
        )


async def text(chat_id: int) -> None:
    async with ClientSession() as session:
        await send_request(
            session,
            METHOD_SEND_MESSAGE,
            json={
                'chat_id': chat_id,
                'text': 'Some text for you',
            }
        )
