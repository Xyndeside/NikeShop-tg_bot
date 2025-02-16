from app.handlers import *
from aiogram import Dispatcher

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(cart_router)
    dp.include_router(contact_router)
    dp.include_router(about_us_router)