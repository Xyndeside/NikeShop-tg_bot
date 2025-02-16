import asyncio
from database import engine, async_session, Base
from models import Product, Category


async def init_db(drop_tables=False):
    if drop_tables:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    categories_data = [
        {"name": 'Sneakers'},
        {"name": 'Hoodies'},
        {"name": 'T-shirts'},
        {"name": 'Accessories'},
        {"name": 'Tracksuits'}
    ]

    products_data = [
        {
            "name": 'Air Force 1',
            "description": 'Sleek, breathable sneakers for city walks and casual style.',
            "imageUrl": '/images/sneakers/1.png',
            "price": 14500,
            "quantity": 3,
            "category": 1
        },
        {
            "name": 'Air Jordan 4',
            "description": 'Rugged outdoor shoes built for tough terrains and adventure seekers.',
            "imageUrl": '/images/sneakers/2.png',
            "price": 35000,
            "quantity": 2,
            "category": 1
        },
        {
            "name": 'Air max 1900',
            "description": 'Lightweight runners perfect for gym workouts and everyday comfort.',
            "imageUrl": '/images/sneakers/3.png',
            "price": 19000,
            "quantity": 6,
            "category": 1
        },
        {
            "name": 'Zoomx',
            "description": 'Stylish tennis-inspired kicks with a modern, sporty edge.',
            "imageUrl": '/images/sneakers/4.png',
            "price": 16300,
            "quantity": 6,
            "category": 1
        },
        {
            "name": 'Shrek run',
            "description": 'Reflective accents and cushioned soles for nighttime joggers.',
            "imageUrl": '/images/sneakers/5.png',
            "price": 21000,
            "quantity": 7,
            "category": 1
        },
        {
            "name": 'Black Mamba',
            "description": 'Soft, oversized hoodie for ultimate comfort and chill vibes.',
            "imageUrl": '/images/hoodies/1.png',
            "price": 5000,
            "quantity": 9,
            "category": 2
        },
        {
            "name": 'White Mamba',
            "description": 'Sleek design with a urban look, perfect for casual outings.',
            "imageUrl": '/images/hoodies/2.png',
            "price": 9000,
            "quantity": 3,
            "category": 2
        },
        {
            "name": 'Red Mamba',
            "description": 'Lightweight yet warm, ideal for layering on cool days.',
            "imageUrl": '/images/hoodies/3.png',
            "price": 7000,
            "quantity": 1,
            "category": 2
        },
        {
            "name": 'White Essential',
            "description": 'Simple, soft cotton tee for everyday effortless style.',
            "imageUrl": '/images/t-shirts/1.png',
            "price": 2500,
            "quantity": 25,
            "category": 3
        },
        {
            "name": 'Red Essential',
            "description": 'Lightweight and moisture-wicking for workouts and beyond.',
            "imageUrl": '/images/t-shirts/2.png',
            "price": 2800,
            "quantity": 30,
            "category": 3
        },
        {
            "name": 'Blue Essential',
            "description": 'Bold graphics and vintage vibes for a standout look.',
            "imageUrl": '/images/t-shirts/3.png',
            "price": 3000,
            "quantity": 19,
            "category": 3
        },
        {
            "name": 'Green bag',
            "description": 'Classic cap with a bold logo, perfect for casual streetwear.',
            "imageUrl": '/images/accessories/1.png',
            "price": 1900,
            "quantity": 43,
            "category": 4
        },
        {
            "name": 'Sport`s backpack',
            "description": 'Sleek, adjustable band for a touch of understated style.',
            "imageUrl": '/images/accessories/2.png',
            "price": 2300,
            "quantity": 35,
            "category": 4
        },
        {
            "name": 'Red Backpack',
            "description": 'Just a red backpack',
            "imageUrl": '/images/accessories/3.png',
            "price": 2100,
            "quantity": 24,
            "category": 4
        }
    ]

    async with async_session() as session:
        for category in categories_data:
            category = Category(**category)
            session.add(category)

        for product in products_data:
            product = Product(**product)
            session.add(product)

        await session.commit()

if __name__ == '__main__':
    asyncio.run(init_db())
