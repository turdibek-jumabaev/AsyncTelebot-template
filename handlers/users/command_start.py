from loader import bot, db
from data.config import ADMINS
from telebot.types import Message

@bot.message_handler(commands=['start'])
async def command_start(message: Message):
    name = message.from_user.full_name

    try:
        db.add_user(id=message.from_user.id, name=name)
    except Exception as e:
        print(e)
    
    await bot.send_message(message.chat.id, f"Salom, {name}")

    count = db.count_users()[0]
    msg = f"{name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi mavjud."
    await bot.send_message(ADMINS[0], msg)