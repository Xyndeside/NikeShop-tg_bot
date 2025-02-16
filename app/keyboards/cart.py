from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cart_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅Place an order', callback_data='place_order')],
        [InlineKeyboardButton(text='❌Empty trash', callback_data='empty_cart')],
        [InlineKeyboardButton(text='Main page', callback_data='to_main')]
    ]
)
