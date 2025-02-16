from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database import requests


async def get_categories_keyboard():
    all_categories = await requests.get_categories()
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))

    keyboard.add(InlineKeyboardButton(text='Main page', callback_data='to_main'))

    return keyboard.adjust(2).as_markup()


async def get_items_keyboard(category_id):
    all_items = await requests.get_category_items(category_id)
    keyboard = InlineKeyboardBuilder()

    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))

    keyboard.add(InlineKeyboardButton(text='Main page', callback_data='to_main'))

    return keyboard.adjust(2).as_markup()

item_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Add to cart', callback_data='add_to_card')],
        [InlineKeyboardButton(text='Main page', callback_data='to_main')]
    ]
)
