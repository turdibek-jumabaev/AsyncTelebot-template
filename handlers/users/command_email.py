from telebot.types import Message
from telebot.asyncio_filters import StateFilter

from loader import bot, db

bot.add_custom_filter(StateFilter(bot))

@bot.message_handler(commands=['email'])
async def command_email(message: Message):
    await bot.send_message(message.chat.id, "Emailingizni kiriting:")
    await bot.set_state(message.chat.id, 'email')

@bot.message_handler(state='email')
async def state_email(message: Message):
    email = message.text
    db.update_user_email(email=email, user_id=message.chat.id)
    user = db.select_user(user_id=message.chat.id)
    await bot.send_message(message.chat.id, f"Baza yangilandi: {user}")
    await bot.set_state(message.chat.id, None)