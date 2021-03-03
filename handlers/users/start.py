from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(f'Hello, {message.from_user.full_name}!')
