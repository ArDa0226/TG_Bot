from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from attr.filters import exclude

BOT_TOKEN = '7393565379:AAF0eftofZCKOuUHWCcmO2gPeSkbhYyw6xo'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def proess_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!'
                         '\nНапиши мне что-нибудь')


@dp.message(Command(commands='help'))
async def process_help_commad(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(
#             text='Данный тип апдейтов не поддерживается '
#                  'методом send_copy'
#         )
#     with open('update.json', 'w') as json_file:
#         json_file.write(message.model_dump_json(indent=4, exclude_none=True))


@dp.message(F.voice)
async def process_sent_voice(message: Message):
    print(message)
    await message.answer(text='Вы отправили голосовое сообщение')
    with open('voice_update.json', 'w') as voice_json:
        voice_json.write(message.model_dump_json(indent=4, exclude_none=True))





if __name__ == '__main__':
    dp.run_polling(bot)
