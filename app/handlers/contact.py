from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards import to_main_kb

router = Router()


@router.callback_query(F.data == 'to_contact')
async def to_contact(callback: CallbackQuery):
    await callback.message.delete()

    text = (
        "👋 Hi! This is the contact section of our bot.\n\n"
        "If you have any questions or issues, here’s how you can contact us:\n"
        "📞 Telegram: [@Xyndeside](https://t.me/Xyndeside)\n"
        "📧 Email: nike-pro@shop.com\n\n"
        "❓ Frequently Asked Questions: [FAQ](link_to_FAQ)\n"
        "⚠️ Found a bug? Use the /report command or contact us on Telegram.\n\n"
        "📄 Privacy Policy: [Privacy Policy](link_to_privacy_policy)\n"
        "📜 Terms of Use: [Terms of Use](link_to_terms_of_use)\n\n"
        "🌟 We value your feedback! Share your thoughts or suggest new features."
    )

    await callback.message.answer(
        text=text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=to_main_kb
    )
