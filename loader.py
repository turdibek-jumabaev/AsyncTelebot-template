from telebot.async_telebot import AsyncTeleBot, ExceptionHandler
from telebot.asyncio_storage import StateMemoryStorage
from data.config import BOT_TOKEN


bot = AsyncTeleBot(BOT_TOKEN, exception_handler=ExceptionHandler(), state_storage=StateMemoryStorage())