import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

cute_messages = [
    "Ти неймовірна 💖",
    "Я дуже радий, що ти є 🌸",
    "Ти робиш цей світ теплішим ✨",
    "Не забувай: ти важлива 💕",
    "Обіймаю тебе 🫂"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт 💕\n"
        "Я твій милий бот 🧸\n\n"
        "Команди:\n"
        "/love — тепле повідомлення 💖\n"
        "/help — допомога"
    )

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(cute_messages))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Доступні команди:\n"
        "/start — почати\n"
        "/love — отримати любов 💕"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
