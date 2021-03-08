from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import CallbackQuery

from keyboards.default import start_menu
from keyboards.inline.callback_datas import jameco_callback
from keyboards.inline import jameco
from loader import dp
from data.dialog import about_college, library


@dp.message_handler(Command('college'))
async def college_info(message: types.Message):
    await message.answer(text='Колледж туралы', reply_markup=jameco)


@dp.callback_query_handler(jameco_callback.filter(btn_name='about'))
async def info_about_college(callback: CallbackQuery):
    await callback.message.answer(text=about_college)


@dp.callback_query_handler(jameco_callback.filter(btn_name='library'))
async def info_about_college(callback: CallbackQuery):
    await callback.message.answer(text=library)


@dp.callback_query_handler(jameco_callback.filter(btn_name='menu'))
async def info_about_college(callback: CallbackQuery):
    await callback.message.answer(f'Главное меню \n\n'
                                  f'/help - 🆘 Services \n'
                                  f'/survey - 🏢 Dormitory\n'
                                  f'/profile - 🏫 College \n'
                                  f'/subs -  👤 Profile \n'
                                  f'/about - 🤖 About Smart Jameco Bot',
                                  reply_markup=start_menu)
