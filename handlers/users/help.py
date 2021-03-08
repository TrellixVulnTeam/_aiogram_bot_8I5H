from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline import service
from keyboards.inline.callback_datas import service_callback
from keyboards.default import start_menu

from loader import dp


@dp.message_handler(Command('help'))
async def show_services(message: types.Message):
    await message.answer(text=f'{message.from_user.username}, select a service',
                         reply_markup=service)


@dp.callback_query_handler(service_callback.filter(service_name='one'))
async def callback_one(callback: CallbackQuery):
    await callback.answer(text='sen tan da din one')


# ---------------Main menu button--------------

@dp.callback_query_handler(service_callback.filter(service_name='menu'))
async def main_menu(call: CallbackQuery):
    await call.message.answer(f'Главное меню \n\n'
                              f'/help - 🆘 Services \n'
                              f'/survey - 🏢 Dormitory\n'
                              f'/profile - 🏫 College \n'
                              f'/subs -  👤 Profile \n'
                              f'/about - 🤖 About Smart Jameco Bot',
                              reply_markup=start_menu)
