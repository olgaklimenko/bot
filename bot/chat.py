# -*- coding: utf-8 -*-
import telepot.aio


class Chat(telepot.aio.helper.ChatHandler):
    async def on_chat_message(self, msg):
        text = \
            ' ```text \n ' \
            'Hello!\n' \
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod fermentum \n' \
            'ornare. Praesent venenatis vestibulum dui, ornare sagittis est elementum at. \n ' \
            'Aenean quis quam dui. Aenean lorem nibh, ultrices at lorem sed, gravida gravida \n  ' \
            'ipsum. Curabitur at consectetur mauris. Phasellus fermentum suscipit purus sed aliquam. \n' \
            'Duis aliquet felis ultrices lacus cursus placerat.\n ``` ' \
            '\n [23432435435](tel:23432435435) \n ' \

        await self.sender.sendMessage(text=text, parse_mode='Markdown')
