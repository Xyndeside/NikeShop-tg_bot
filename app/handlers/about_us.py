from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards import to_main_kb

router = Router()


@router.callback_query(F.data == 'to_infoAboutUs')
async def to_infoAboutUs(callback: CallbackQuery):
    await callback.message.delete()

    text = (
        "🌟 About Us\n\n"
        "Welcome to the official Nike store! At Nike, we believe in the power of sport and innovation to transform lives. "
        "Our mission is to bring inspiration and innovation to every athlete* in the world (*and if you have a body, you’re an athlete).\n\n"
        "👟 What We Stand For:\n"
        "- **Innovation**: We push boundaries with cutting-edge technology in every product we create.\n"
        "- **Performance**: From running shoes to athletic wear, we design gear to help you achieve your personal best.\n"
        "- **Sustainability**: We are committed to reducing our environmental impact and creating a better future for sport.\n\n"
        "🏆 Our Story:\n"
        "Founded in 1964 as Blue Ribbon Sports, Nike has grown into a global leader in sportswear and athletic performance. "
        "From the iconic Swoosh logo to groundbreaking innovations like Air cushioning and Flyknit technology, Nike continues to redefine what’s possible in sport and style.\n\n"
        "🌍 Join the Movement:\n"
        "Whether you're a professional athlete, a weekend warrior, or just starting your fitness journey, Nike is here to support you every step of the way. "
        "Explore our collection of footwear, apparel, and accessories designed to inspire greatness.\n\n"
        "💬 Questions? Suggestions?\n"
        "We’d love to hear from you! Visit our [Contact Us](ссылка_на_контакты) section or reach out to us on Telegram: [@Xyndeside](https://t.me/Xyndeside)."
    )

    await callback.message.answer(
        text=text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=to_main_kb
    )