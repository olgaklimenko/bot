# -*- coding: utf-8 -*-
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    async def on_chat_message(self, msg):
        text = 'Hello ! [2343243543](tel:+79996201512) Hello'
        await self.sender.sendMessage(text=text, parse_mode='Markdown')
