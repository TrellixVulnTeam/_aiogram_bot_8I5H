from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS

from loader import dp


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    for admin in ADMINS:
        await dp.bot.send_message(admin, f'Bot was run by {message.from_user.full_name}')
    await message.answer(f'Hello, {message.from_user.full_name}!')
