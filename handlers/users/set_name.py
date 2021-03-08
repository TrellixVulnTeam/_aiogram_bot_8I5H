from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command

from states import SetName


@dp.message_handler(Command('setname'))
async def set_user_name(message: types.Message):
    await message.answer(text='How can I call you? \n'
                              'You can answer: \n')

    await SetName.get_nick_name.set()


@dp.message_handler(state=SetName.get_nick_name)
async def answer_1(message: types.Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer1'] = answer
    await message.answer(text=f'your name is {data["answer1"]}')
