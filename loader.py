from utils.db_api.sqlite import Datebase
from telebot.async_telebot import AsyncTeleBot, ExceptionHandler
from data.config import BOT_TOKEN

db = Datebase(path_to_db="data/main.db")

bot = AsyncTeleBot(BOT_TOKEN, exception_handler=ExceptionHandler())