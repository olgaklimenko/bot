# -*- coding: utf-8 -*-
import settings
import telepot
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Chat, self).__init__(*args, **kwargs)

    async def on_chat_message(self, msg, **kwargs):
        if not kwargs.get('parse_mode'):
            kwargs['parse_mode'] = 'HTML'
        await self.sender.sendMessage('<h1>Hello</h1>', **kwargs)