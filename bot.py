from loader import bot 
import asyncio
import middlewares
import handlers
import utils

asyncio.run(bot.infinity_polling(skip_pending=True))