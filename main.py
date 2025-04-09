from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

FILE_PATH = 'langeta.rar'  # замени на путь к твоему файлу


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Получить файл", callback_data='send_file')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Напиши мне запрос, и по нему я спроектирую лангету.", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):



    wait_msg = await update.message.reply_text("🔍 Подготовка файла...")

    dots = ["⏳", "⌛", "⏳", "⌛"",⏳", "⌛"]
    for dot in dots:
        await asyncio.sleep(1)  # Задержка 1 секунда
        await wait_msg.edit_text(f"Файл загружается {dot}")

    with open(FILE_PATH, 'rb') as f:
        await update.message.reply_document(document=f, filename=FILE_PATH.split("/")[-1])

    await wait_msg.delete()


if __name__ == '__main__':
    TOKEN = "7709229308:AAEMYz2B2VYPlQ6yCFV-AkaB5aQ1QU2oosI"  # можно заменить на строку токена прямо

    app = ApplicationBuilder().token(TOKEN).read_timeout(7).write_timeout(7).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling()