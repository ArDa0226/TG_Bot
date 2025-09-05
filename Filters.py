from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7393565379:AAF0eftofZCKOuUHWCcmO2gPeSkbhYyw6xo'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def my_start_filter(message: Message):
    return message.text and message.text == '/start'

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)