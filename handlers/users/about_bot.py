from aiogram import types
from aiogram.dispatcher.filters import Command
from data.dialog import information_about_bot
from loader import dp


@dp.message_handler(Command('about'))
async def about_bot(message: types.Message):
    await message.answer(text=information_about_bot)
