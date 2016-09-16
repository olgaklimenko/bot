# -*- coding: utf-8 -*-
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    async def on_chat_message(self, msg):
        await self.sender.sendMessage('[Hello](http://google.com/)', parse_mode='Markdown')
