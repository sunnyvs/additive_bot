from email.message import Message

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import asyncio

FILE_PATH = 'langeta.rar'  # замени на путь к твоему файлу


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я Аддитивный GPT!👾\nОтправьте мне техническое задание и я сделаю цифровую модель.")

async def handle_all_input(update: Update, context: ContextTypes.DEFAULT_TYPE):



    wait_msg = await update.message.reply_text("🔍 Подготовка файла...")

    dots = ["⏳", "⌛", "⏳", "⌛","⏳", "⌛"]
    for dot in dots:
        await asyncio.sleep(1)  # Задержка 1 секунда
        await wait_msg.edit_text(f"Файл загружается {dot}")

    with open(FILE_PATH, 'rb') as f:
        await update.message.reply_document(document=f, filename=FILE_PATH.split("/")[-1])

    await wait_msg.delete()


if __name__ == '__main__':
    TOKEN = "7709229308:AAEMYz2B2VYPlQ6yCFV-AkaB5aQ1QU2oosI"

    app = ApplicationBuilder().token(TOKEN).read_timeout(7).write_timeout(7).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT | filters.Document.ALL, handle_all_input))
    app.run_polling()