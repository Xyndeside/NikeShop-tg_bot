from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.keyboards import get_categories_keyboard, get_items_keyboard
from app.utils.handlers_utils import sendPhoto
from app.database import requests
from app.states import CartState

router = Router()


@router.callback_query(F.data == 'to_catalog')
async def to_catalog(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Categories', reply_markup=await get_categories_keyboard())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.message.delete()
    category_id = callback.data.split('_')[1]
    await callback.message.answer('Choose product', reply_markup=await get_items_keyboard(int(category_id)))


@router.callback_query(F.data.startswith('item_'))
async def item(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    item_id = int(callback.data.split('_')[1])

    await state.set_state(CartState.item_selected)
    await state.update_data(item_id=item_id)

    item_data = await requests.get_item(item_id)
    image_path = f'static/{item_data.imageUrl}'

    await sendPhoto(callback, image_path, item_data)


@router.callback_query(F.data == 'add_to_card')
async def add_to_card(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()

    if current_state != CartState.item_selected:
        await callback.answer("Error: product is not selected.")
        return

    data = await state.get_data()
    item_id = data.get('item_id')
    user_id = callback.from_user.id

    if not item_id:
        await callback.answer("Error. Try again later.")
        return

    await requests.set_cart_item(user_id, item_id)
    await callback.answer(f"Product added to cart.")


