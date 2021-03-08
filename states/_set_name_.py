from aiogram.dispatcher.filters.state import StatesGroup, State


class SetName(StatesGroup):
    get_nick_name = State()
    get_user_full_name = State()
    get_phone_number = State()
    get_user_mail_address = State()
