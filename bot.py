from loader import bot, db
import asyncio
import middlewares
import handlers
import utils

try:
    db.create_table_users()
except Exception as e:
    print(e)

asyncio.run(bot.infinity_polling(skip_pending=True))