from app.database import async_session
from app.database import Category, Product, Cart, User
from sqlalchemy import select, delete, exists


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def get_category_items(category_id):
    async with async_session() as session:
        return await session.scalars(select(Product).where(Product.category == category_id))


async def get_item(id):
    async with async_session() as session:
        return await session.scalar(select(Product).where(Product.id == id))


async def get_category(category_id):
    async with async_session() as session:
        return await session.scalar(select(Category).where(Category.id == category_id))


async def set_cart_item(user_id, product_id):
    async with async_session() as session:
        cart_item = await session.scalar(select(Cart).where(Cart.user_id == user_id, Cart.product_id == product_id))

        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = Cart(user_id=user_id, product_id=product_id, quantity=1)
            session.add(cart_item)

        await session.commit()


async def get_cart_items(user_id):
    async with async_session() as session:
        return await session.scalars(select(Cart).where(Cart.user_id == user_id))

async def remove_carts_by_userId(user_id):
    async with async_session() as session:
        cart_exists = await session.scalar(
            select(exists().where(Cart.user_id == user_id))
        )

        if not cart_exists:
            raise Exception("Cart is empty")

        await session.execute(
            delete(Cart).where(Cart.user_id == user_id)
        )

        await session.commit()
