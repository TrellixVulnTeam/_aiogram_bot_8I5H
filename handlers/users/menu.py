from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from keyboards.default import menu

from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Choose good from loader',
                         reply_markup=menu)


@dp.message_handler(Text(equals=['2', '3']))
async def show_food(message: types.Message):
    await message.reply(text=f'you have chosen {message.text}',
                        reply_markup=ReplyKeyboardRemove())

