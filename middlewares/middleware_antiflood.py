from loader import bot 

from telebot.asyncio_handler_backends import BaseMiddleware
from telebot.async_telebot import CancelUpdate

class SimpleMiddleware(BaseMiddleware):
    def __init__(self, limit) -> None:
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']

    async def pre_process(self, message, data):
        if not message.from_user.id in self.last_time:
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            await bot.send_message(message.chat.id, 'Siz juda ko\'p murojaat qilyabsiz!')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    async def post_process(self, message, data, exception):
        pass
bot.setup_middleware(SimpleMiddleware(limit=2))