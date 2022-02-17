from loader import bot
import telebot

class IsPrivate(telebot.asyncio_filters.SimpleCustomFilter):
    key = 'is_private'
    @staticmethod
    async def filter(message):
        return message.chat.type == 'private'
    
bot.add_custom_filter(IsPrivate())