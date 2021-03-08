from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import jameco_callback

jameco = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='Колледж туралы',
                                                           callback_data=jameco_callback.new(btn_name='about')),
                                      InlineKeyboardButton(text='Мамандықтар',
                                                           callback_data=jameco_callback.new(btn_name='professions'))
                                  ],
                                  [
                                      InlineKeyboardButton(text='Кітапхана туралы',
                                                           callback_data=jameco_callback.new(btn_name='library')),
                                      InlineKeyboardButton(text='Мекен жай',
                                                           callback_data=jameco_callback.new(btn_name='address'))
                                  ],
                                  [
                                      InlineKeyboardButton(text='Кері байланыс',
                                                           callback_data=jameco_callback.new(btn_name='callback'))
                                  ],
                                  [
                                      InlineKeyboardButton(text='Main menu',
                                                           callback_data=jameco_callback.new(btn_name='menu'))
                                  ]
                              ])

cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Cancel', callback_data=jameco_callback.new('jameco'))
    ]
])
