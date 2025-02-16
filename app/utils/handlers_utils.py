from aiogram.types import FSInputFile

from app.database import Product
from app.keyboards import item_keyboard, cart_keyboard
from app.database import requests


async def sendPhoto(callback, imagePath, item_data: Product):
    try:
        photo = FSInputFile(imagePath)
        chat_id = callback.from_user.id

        await callback.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=f'{item_data.name}\n\n{item_data.description}\n\nLeft in stock: {item_data.quantity}\n\nPrice: {item_data.price}',
            reply_markup=item_keyboard
        )
    except Exception as e:
        print("Ошибка при отправке фото:", e)
        await callback.message.delete()
        await callback.message.answer("Something went wrong.")


async def showCart(callback, user_id):
    cart_items = await requests.get_cart_items(user_id)

    if not cart_items:
        await callback.message.answer("Your cart is empty.")
        return

    cart_text = "🛒 Your cart:\n"
    total_price = 0

    for item in cart_items:
        product = await requests.get_item(item.product_id)
        cart_text += (
            f"- {product.name} ({product.price} rub.) x {item.quantity} "
            f"= {product.price * item.quantity} rub.\n"
        )
        total_price += product.price * item.quantity

    cart_text += f"\nTotal price: {total_price} rub."

    await callback.message.delete()
    await callback.message.answer(cart_text, reply_markup=cart_keyboard)
