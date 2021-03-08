from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold, hlink
from data.config import ADMINS
from data.dialog import information_about_bot
from keyboards.default import start_menu
from keyboards.inline import service, jameco
from loader import dp
from states import SetName


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


# ------------------------------All Information About Bot-------------------------------
@dp.message_handler(Text(equals='🤖 About Smart Jameco Bot'))
async def bot_info(message: types.Message):
    await message.answer(text=information_about_bot, reply_markup=ReplyKeyboardRemove())


# ------------------------------There Inline buttons about College-------------------------------
@dp.message_handler(Text(equals='🏫 College'))
async def college_info(message: types.Message):
    await message.answer(text=f'{message.from_user.username}, қызметті таңдаңыз', reply_markup=jameco)


# ------------------------------All Information About User(e-mail, phone, number, etc.)-------------------------------
@dp.message_handler(Text(equals='👤 Profile'))
async def get_user_info(message: types.Message):
    await message.answer(text="Your fullname is...")

    await SetName.get_user_full_name.set()


@dp.message_handler(state=SetName.get_user_full_name)
async def full_name(message: types.Message, state: FSMContext):
    user_full_name = message.text

    await state.update_data(user_full_name=user_full_name)

    await message.answer(text='Your phone number...')
    await SetName.get_phone_number.set()


@dp.message_handler(state=SetName.get_phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    user_phone_number = message.text

    await state.update_data(user_phone_number=user_phone_number)

    await message.answer(text='Your E-mail address...')
    await SetName.get_user_mail_address.set()


@dp.message_handler(state=SetName.get_user_mail_address)
async def get_e_mail_address(message: types.Message, state: FSMContext):
    user_mail_address = message.text

    await state.update_data(user_mail_address=user_mail_address)

    data = await state.get_data()
    nick_name = message.from_user.username
    user_full_name = data.get('user_full_name')
    user_phone_number = data.get('user_phone_number')
    user_e_mail_address = data.get('user_mail_address')

    await message.answer(text="Your profile:\n"
                              f"Имя пользователя: {nick_name}\n"
                              f"ФИО: {user_full_name}\n"
                              f"Номер телефона: {user_phone_number}\n"
                              f"E-mail: {user_e_mail_address}")

    await state.reset_state(with_data=False)
