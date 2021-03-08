from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold
from data.config import ADMINS
from data.dialog import information_about_bot
from keyboards.default import start_menu
from keyboards.inline import service, jameco
from loader import dp


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    for admin in ADMINS:
        await dp.bot.send_message(admin, f'Bot was run by {message.from_user.full_name}')
    await message.answer(f'Hello, {message.from_user.full_name}!\n')
    await message.answer(f'Главное меню \n\n'
                         f'/help - 🆘 Services \n'
                         f'/survey - 🏢 Dormitory\n'
                         f'/college - 🏫 College \n'
                         f'/subs -  👤 Profile \n'
                         f'/about - 🤖 About Smart Jameco Bot',
                         reply_markup=start_menu)


@dp.message_handler(Text(equals='🆘 Services'))
async def show_services(message: types.Message):
    await message.answer(text=f'{message.from_user.username}, select a service',
                         reply_markup=service)


@dp.message_handler(Text(equals='🤖 About Smart Jameco Bot'))
async def bot_info(message: types.Message):
    await message.answer(text=information_about_bot, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals='👤 Profile'))
async def get_user_info(msg: types.Message):
    await msg.answer(text=f'{hbold("Имя пользователя: ")} {msg.from_user.username}\n'
                          f'{hbold("ФИО: ")}-\n'
                          f'{hbold("Номер телефона: ")}-\n'
                          f'{hbold("E-mail: ")}-\n'
                          f'{hbold("Язык по умолчанию: ")}-')


# ------------------------------There Inline buttons about College-------------------------------
@dp.message_handler(Text(equals='🏫 College'))
async def college_info(message: types.Message):
    await message.answer(text='Hi there', reply_markup=jameco)
    await message.answer(text='Ok', reply_markup=ReplyKeyboardRemove())

