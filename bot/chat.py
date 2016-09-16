# -*- coding: utf-8 -*-
import settings
import telepot
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Chat, self).__init__(*args, **kwargs)

    async def on_chat_message(self, msg):
        await self.sender.sendMessage('[Hello](http://google.com/)', parse_mode='Markdown')
