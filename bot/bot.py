import telepot
import asyncio
import settings
from telepot.delegate import per_chat_id
from telepot.aio.delegate import create_open, pave_event_space
from bot.chat import Chat


class Bot(object):

    def __init__(self, token):
        self.token = token
        self.telepot = telepot.aio.DelegatorBot(self.token, [
            pave_event_space()
            (
                per_chat_id,
                create_open,
                Chat,
                timeout=100
            )
        ])

    def run_forever(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.telepot.message_loop())
        loop.run_forever()




