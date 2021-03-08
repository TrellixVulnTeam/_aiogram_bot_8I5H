from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from keyboards.default import start_menu
from keyboards.inline.callback_datas import jameco_callback
from keyboards.inline import jameco, cancel
from loader import dp, bot
from data.dialog import about_college, library, professions, address, call_back, required_documents


# ---------------------------Main Menu About College-----------------------
@dp.message_handler(Command('college'))
async def college_info(message: types.Message):
    await message.answer(text=f'{message.from_user.username}, қызметті таңдаңыз', reply_markup=jameco)


# ---------------------------Information About College-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='about'))
async def info_about_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=about_college,
                                reply_markup=cancel)


# ---------------------------Information About Library-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='library'))
async def info_about_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=library,
                                reply_markup=cancel)


# ---------------------------Information About Professions-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='professions'))
async def info_about_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=professions,
                                reply_markup=cancel)


# ---------------------------Information About Address-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='address'))
async def info_about_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=address,
                                reply_markup=cancel)


# ---------------------------Information About Address-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='callback'))
async def info_about_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=call_back,
                                reply_markup=cancel)


# ---------------------------TO Enter College-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='to_enter_college'))
async def to_enter_college(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text=required_documents,
                                reply_markup=cancel)

# ---------------------------Back to Main Menu-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='menu'))
async def info_about_college(callback: CallbackQuery):
    await callback.message.answer(f'Главное меню \n\n'
                                  f'/help - 🆘 Services \n'
                                  f'/survey - 🏢 Dormitory\n'
                                  f'/college - 🏫 College \n'
                                  f'/profile -  👤 Profile \n'
                                  f'/about - 🤖 About Smart Jameco Bot',
                                  reply_markup=start_menu)


# ---------------------------Cancel Button and Back to Main Menu-----------------------
@dp.callback_query_handler(jameco_callback.filter(btn_name='jameco'))
async def college_info(message: CallbackQuery):
    await bot.edit_message_text(message_id=message.message.message_id,
                                chat_id=message.message.chat.id,
                                reply_markup=jameco,
                                text=f'{message.from_user.username}, қызметті таңдаңыз')
