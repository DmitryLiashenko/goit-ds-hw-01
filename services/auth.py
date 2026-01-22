import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

AUTHORIZED_USERS = set()

ALLOWED_ADMINS = os.getenv("ALLOWED_USERNAMES", "").split(",")
ALLOWED_PHONES = os.getenv("ALLOWED_PHONES", "").split(",")


def is_admin(identifier: str) -> bool:
    return identifier in ALLOWED_ADMINS


def authorize_user(identifier: str, is_admin_flag=False) -> bool:
    if is_admin_flag and identifier in ALLOWED_ADMINS:
        AUTHORIZED_USERS.add(identifier)
        return True
    if identifier in ALLOWED_PHONES:
        AUTHORIZED_USERS.add(identifier)
        return True
    return False


def is_user_authorized(identifier: str) -> bool:
    return identifier in AUTHORIZED_USERS


async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact

    if contact.user_id != update.effective_user.id:
        await update.message.reply_text("❗️Пожалуйста, отправьте СВОЙ номер телефона.")
        return

    phone = contact.phone_number.replace("+", "")
    if authorize_user(phone):
        context.user_data["identifier"] = phone
        context.user_data["is_admin"] = False
        await update.message.reply_text("✅ Вы успешно авторизованы по номеру.")
    else:
        await update.message.reply_text("⛔️ Ваш номер не найден в списке разрешённых.")
