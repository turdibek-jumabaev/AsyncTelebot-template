from loader import bot 
from states.personData import PersonData

from telebot.asyncio_filters import StateFilter
from telebot.types import Message

bot.add_custom_filter(StateFilter(bot))

@bot.message_handler(commands=['register'])
async def register(message: Message):
    await bot.send_message(message.chat.id, 'Ismingizni kiriting')
    await bot.set_state(user_id=message.from_user.id, state=PersonData.fullname, chat_id=message.chat.id)

@bot.message_handler(state="*", commands=['cancel'])
async def cancel(message: Message):
    await bot.send_message(message.chat.id, 'Ro\'yhatdan o\'tish bekor qilindi')
    await bot.delete_state(message.chat.id)

@bot.message_handler(state=PersonData.fullname)
async def fullname(message: Message):
    async with bot.retrieve_data(message.from_user.id, chat_id=message.chat.id) as data:
        data['fullname'] = message.text
    
    await bot.send_message(message.chat.id, 'Yoshini kiriting')
    await bot.set_state(user_id=message.from_user.id, state=PersonData.age, chat_id=message.chat.id)

@bot.message_handler(state=PersonData.age)
async def age(message: Message):
    async with bot.retrieve_data(message.from_user.id, chat_id=message.chat.id) as data:
        data['age'] = message.text

    await bot.send_message(message.chat.id, 'Telefon raqamingizni kiriting')
    await bot.set_state(user_id=message.from_user.id, state=PersonData.phone, chat_id=message.chat.id)

@bot.message_handler(state=PersonData.phone)
async def phone(message: Message):
    async with bot.retrieve_data(message.from_user.id, chat_id=message.chat.id) as data:
        data['phone'] = message.text
    
    matn = f"Siz ro'yhatdan o'tdingiz.\n\n"
    matn += f"Ismingiz: {data['fullname']}\n"
    matn += f"Yosh: {data['age']}\n"
    matn += f"Telefon raqami: {data['phone']}\n"

    await bot.send_message(message.chat.id, matn)
    await bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)