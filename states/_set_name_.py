from aiogram.dispatcher.filters.state import StatesGroup, State


class SetName(StatesGroup):
    get_nick_name = State()
