from loader import bot 
from telebot.types import Message

@bot.message_handler(commands=['help'])
async def command_help(message: Message):
    await bot.send_message(chat_id = message.chat.id, text = "Yordam:\n/start - botni qayta ishga tushirish\n/help - yordam")