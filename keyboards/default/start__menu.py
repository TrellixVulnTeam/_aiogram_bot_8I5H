from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🆘 Services'),
            KeyboardButton(text='🏢 Dormitory')
        ],
        [
            KeyboardButton(text='🏫 College'),
            KeyboardButton(text='👤 Profile')
        ],
        [
            KeyboardButton(text='🤖 About Smart Jameco Bot')
        ]
    ],
    resize_keyboard=True
)
