from loader import bot

@bot.message_handler(func=lambda message: True)
async def echo(message):
    await bot.send_message(chat_id=message.chat.id, text=message.text)