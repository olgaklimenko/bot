# -*- coding: utf-8 -*-
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    async def on_message(self, msg, **kwargs):
        if not kwargs.get('parse_mode'):
            kwargs['parse_mode'] = 'Markdown'
        await self.sender.sendMessage('# Hello\n *test*', **kwargs)
