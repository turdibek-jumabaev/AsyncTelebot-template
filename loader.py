from telebot.async_telebot import AsyncTeleBot, ExceptionHandler
from data.config import BOT_TOKEN


bot = AsyncTeleBot(BOT_TOKEN, exception_handler=ExceptionHandler())