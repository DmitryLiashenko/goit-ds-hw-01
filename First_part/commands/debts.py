from telegram import Update
from telegram.ext import ContextTypes
from services.get_last_modified import get_last_modified
from services.google_sheets import (
    get_debts_data_admin,
    get_debts_data_user,
    creds,
    SOURCE_SPREADSHEET_ID,
)


async def debts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    identifier = context.user_data.get("identifier")
    is_admin = context.user_data.get("is_admin", False)

    if not identifier:
        await update.message.reply_text(
            "Пожалуйста, авторизируйтесь через команду /start."
        )
        return

    try:
        if is_admin:
            result_messages = get_debts_data_admin()
        else:
            result_messages = get_debts_data_user(identifier)

        for message in result_messages:
            await update.message.reply_text(message, parse_mode="Markdown")

        formatted_time = get_last_modified(creds, SOURCE_SPREADSHEET_ID)
        await update.message.reply_text(
            f"📅 Последнее обновление таблицы: {formatted_time}"
        )

        if is_admin and int(result_messages[-1].splitlines()[-1]) < 0:
            await update.message.reply_text(
                "💸 Касса в минусе — пора сдавать бутылки!\n👷‍♂️ Мужики, когда работать будете?!"
            )
        elif is_admin:
            await update.message.reply_text("О, можно и поделить денюжку)))")

    except Exception as e:
        await update.message.reply_text(f"❗️Произошла ошибка: {e}")
