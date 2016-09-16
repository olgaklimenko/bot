import sys
from bot.bot import Bot
import settings

if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
else:
    TOKEN = settings.TOKEN

bot = Bot(TOKEN)
print('Listening ...')
bot.run_forever()
