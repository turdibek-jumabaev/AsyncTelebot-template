from loader import bot 
from telebot.types import Message

@bot.message_handler(commands=['start'])
async def command_start(message: Message):
    await bot.send_message(chat_id = message.chat.id, text = f'Assalomu alaykum! {message.from_user.full_name}')
