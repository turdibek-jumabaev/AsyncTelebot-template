from loader import bot
from data.config import ADMINS
import asyncio

async def notify_admins(message):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, message)
        except:
            pass

asyncio.run(notify_admins("Bot ishga tushdi!"))