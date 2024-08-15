import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InputFile

# Получение API токена из переменной окружения
API_TOKEN = os.getenv("7502771695:AAG29JRkQR6eP0llIvAEszIHUnz8L4yeftQ")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Хэндлер для команды /start
@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Выбрать дизайн 1')
    button2 = KeyboardButton('Выбрать дизайн 2')
    keyboard.add(button1, button2)
    await message.reply("Добро пожаловать в игру! Выберите дизайн карт:", reply_markup=keyboard)

# Хэндлеры для выбора дизайна карт
@dp.message_handler(lambda message: message.text in ["Выбрать дизайн 1", "Выбрать дизайн 2"])
async def choose_design(message: types.Message):
    if message.text == "Выбрать дизайн 1":
        design_folder = "card_designs/design1/"
    else:
        design_folder = "card_designs/design2/"

    # Пример загрузки карты (замените на реальное имя файла)
    card = InputFile(f"{design_folder}ace_of_spades.png")
    await bot.send_photo(message.chat.id, card, caption="Вы выбрали этот дизайн карт!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
 
