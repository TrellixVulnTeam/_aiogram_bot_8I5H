from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🆘 Services'),
            KeyboardButton(text='🏢 Dormitory')
        ],
        [
            KeyboardButton(text='👤 Profile'),
            KeyboardButton(text='🏫 College')
        ],
        [
            KeyboardButton(text='🤖 About Smart Jameco Bot')
        ]
    ],
    resize_keyboard=True
)
