import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" Получить промокод"), KeyboardButton(text=" Участвовать в розыгрыше")],
        [KeyboardButton(text=" Как участвовать"), KeyboardButton(text=" Мои шансы")],
        [KeyboardButton(text=" Правила акции")]
    ],
    resize_keyboard=True
)
@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        "Добро пожаловать в Бот розыгрышей \n\n"
        "Выбери интересующий тебя пункт меню ниже:"
    )
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот успешно запущен и ожидает сообщения...")
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен!")
