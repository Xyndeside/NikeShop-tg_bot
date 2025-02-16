from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.utils.handlers_utils import showCart
from app.database import requests
from app.keyboards import to_main_kb

router = Router()


@router.callback_query(F.data == 'to_cart')
async def to_cart(callback: CallbackQuery):
    await showCart(callback, callback.from_user.id)


@router.callback_query(F.data == 'empty_cart')
async def empty_cart(callback: CallbackQuery):
    try:
        await requests.remove_carts_by_userId(callback.from_user.id)
        await showCart(callback, callback.from_user.id)
    except Exception as e:
        print(e)
        await callback.message.answer("Couldn't remove carts by userID")


@router.callback_query(F.data == 'place_order')
async def place_order(callback: CallbackQuery):
    await callback.message.delete()

    try:
        await requests.remove_carts_by_userId(callback.from_user.id)
        await callback.message.answer('Payment is successful', reply_markup=to_main_kb)
    except Exception as e:
        await callback.message.answer("Error: " + e.__str__(), reply_markup=to_main_kb)
