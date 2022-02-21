from telebot.asyncio_handler_backends import State, StatesGroup

class PersonData(StatesGroup):
    fullname = State()
    age = State()
    phone = State()