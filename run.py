import sys
import asyncio
import telepot
from telepot.aio.delegate import per_chat_id, create_open, pave_event_space
from bot.chat import Chat

if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
else:
    print('Put your bot\'s token as argv to run.py')
    exit(0)

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()
    (
        per_chat_id,
        create_open,
        Chat,
        timeout=100
    )
])
loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop())
loop.run_forever()
print('Listening ...')
