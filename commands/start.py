from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from services.auth import authorize_user, is_user_authorized, is_admin
from services.notifications import notify_admin


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    if user.username and is_admin(user.username):
        identifier = user.username
        if authorize_user(identifier, is_admin_flag=True):
            context.user_data["identifier"] = identifier
            context.user_data["is_admin"] = True
            await update.message.reply_text(
                f"Привет, @{identifier}! Вы успешно авторизованы как админ."
            )
            await notify_admin(context.bot, update, "✅ Админ авторизован", context)
            return

    identifier = context.user_data.get("identifier")
    if identifier and is_user_authorized(identifier):
        await update.message.reply_text(
            f"Привет, {identifier}! Вы уже авторизованы ранее."
        )
        return

    button = KeyboardButton("📱 Поделиться номером", request_contact=True)
    keyboard = [[button]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )

    await update.message.reply_text(
        "У вас не установлен username или вы не админ.\n"
        "Пожалуйста, нажмите кнопку ниже, чтобы поделиться номером телефона для авторизации:",
        reply_markup=reply_markup,
    )
