import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.choice_button import choice, michel_keyboard
from keyboards.inline.callback_datas import friend_callback

from loader import dp
from aiogram import types


@dp.message_handler(Command('test'))
async def testing_inline_keyboard(message: types.Message):
    await message.answer(text='Менын екы досым бар, \n'
                         'Сен кайссын танисын',
                         reply_markup=choice)


@dp.callback_query_handler(friend_callback.filter(friend_name='First'))
async def first_def(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    age = callback_data.get('friend_age')
    await call.message.answer(f'You have chosen First, age {age}, Thank you very much',
                              reply_markup=michel_keyboard)


@dp.callback_query_handler(friend_callback.filter(friend_name='Second'))
async def second_def(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'You have chosen Michel, Thank you very much')


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
    await call.answer('This is alert message ❌', show_alert=True)
    await call.message.edit_reply_markup()