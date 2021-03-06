from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import friend_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='First InlineButton',
                                                           callback_data=friend_callback.new(friend_name='First')
                                                           ),
                                      InlineKeyboardButton(text='Second InlineButton',
                                                           callback_data=friend_callback.new(friend_name='Second')
                                                           )

                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Button for cancel',
                                          callback_data='cancel')
                                  ]
                              ])


michel_keyboard = InlineKeyboardMarkup()

LINK = 'https://go.smarttradecoin.com/'
link = InlineKeyboardButton(text='Here', url=LINK)

michel_keyboard.insert(link)
