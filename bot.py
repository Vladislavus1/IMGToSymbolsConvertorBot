from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
import logging
import db
import convertor
import random
import string
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'your_token'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def set_bot_commands():
    await bot.set_my_commands([
        types.BotCommand("start", "Start a bot"),
        types.BotCommand("help", "Help"),
    ])


async def on_startup(dispatcher):
    await set_bot_commands()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    user = db.get_user(user_id)
    if user == []:
        db.add_user(user_name, user_id)
        await message.answer("<b>Welcome to <code><b>\nI</b>(Image)\n<b>T</b>(To)\n<b>S</b>(Symbols)\n<b>C</b>(Convertor) Bot(ver: <u>030524.1235</u>)</code></b>.\n\nUnlock the power of symbolic image conversion with our innovative bot by sending as an image that you wish to convert.", parse_mode=ParseMode.HTML)
    else:
        await message.answer(f"Welcome back, <b>{message.from_user.first_name}</b>!", parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Github", url="https://github.com/Vladislavus1/IMGToSymbolsConvertorBot")
        ],
        [
            InlineKeyboardButton(text="Official aiogram page", url="https://aiogram.dev")
        ]
    ], row_width=1)
    await message.answer_photo(photo="https://i.ibb.co/cTBKf6J/help-lable.png", caption="<u><i>Instructions for use:</i></u>\n1.<b>Send Your Image</b>: Share the image you desire to convert into text composed of symbols with the bot.\n2.<b>Await Results</b>: Relax while the bot diligently processes your image and swiftly generates the symbolic text representation.\n3.<b>Copy and Utilize</b>: Once the conversion is complete, the bot will promptly deliver the symbolic text to you. Copy the text and unleash your creativity in its usage!\n\nOur bot is not only a marvel in image-to-text conversion but is also fully open-source and freely accessible. Feel free to explore the code and contribute to its development on our GitHub repository.\n\nExperience the magic of image-to-text conversion with our community-driven and open-source bot.", parse_mode=ParseMode.HTML, reply_markup=inline_keyboard)


@dp.message_handler(content_types=['photo'])
async def covert_photo(message: types.Message):
    photo_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15)) + ".jpg"
    await message.photo[-1].download(f"photos/{photo_name}")
    text_name = convertor.convert(photo_name)
    os.remove(f"photos/{photo_name}")
    file = types.InputFile(text_name)
    await message.reply_document(file, caption=f'<i>Photo is successfully converted and ready to utilize!</i>', parse_mode=ParseMode.HTML)
    os.remove(text_name)

if __name__ == '__main__':
    db.run_db()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)