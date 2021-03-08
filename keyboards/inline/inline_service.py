from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import service_callback

service = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='1',
                                                            callback_data=service_callback.new(service_name='one'))
                                   ],
                                   [
                                       InlineKeyboardButton(text='2',
                                                            callback_data=service_callback.new(service_name='two'))
                                   ],
                                   [
                                       InlineKeyboardButton(text='3',
                                                            callback_data=service_callback.new(service_name='three'))
                                   ],
                                   [
                                       InlineKeyboardButton(text='4',
                                                            callback_data=service_callback.new(service_name='four'))
                                   ],
                                   [
                                       InlineKeyboardButton(text='Main menu',
                                                            callback_data=service_callback.new(service_name='menu'))
                                   ]
                               ])
