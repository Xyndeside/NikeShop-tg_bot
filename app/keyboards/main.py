from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Catalog', callback_data='to_catalog')],
        [InlineKeyboardButton(text='Cart', callback_data='to_cart')],
        [InlineKeyboardButton(text='Contact', callback_data='to_contact')],
        [InlineKeyboardButton(text='About us', callback_data='to_infoAboutUs')]
    ],
    resize_keyboard=True
)

to_main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Main page', callback_data='to_main')]
    ]
)