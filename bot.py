from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7502771695:AAG29JRkQR6eP0llIvAEszIHUnz8L4yeftQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
