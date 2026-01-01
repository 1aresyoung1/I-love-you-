import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# 🔐 Беремо токен ТІЛЬКИ з Railway Variables
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("8342609349:AAHpFcc-mY735PX4D6w5pjQLIncJP1bbeyA")

# ===== КОМАНДИ =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["😊 Добре", "😐 Нормально"],
        ["😔 Сумно", "💖 Підтримка"]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Привіт 💕\nЯ твій милий бот 🤖\nЯк ти себе почуваєш?",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧸 Я вмію:\n"
        "/start — почати\n"
        "/help — допомога\n\n"
        "Просто натискай кнопки 💖"
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "😊 Добре":
        await update.message.reply_text("Я дуже рада це чути 😄✨")
    elif text == "😐 Нормально":
        await update.message.reply_text("Головне — що не погано 🌤️")
    elif text == "😔 Сумно":
        await update.message.reply_text("Я поруч 🤍 Хочеш обійми? 🫂")
    elif text == "💖 Підтримка":
        await update.message.reply_text("Ти важлива 💕 І все буде добре 🌸")
    else:
        await update.message.reply_text("Я тебе слухаю 👂💭")

# ===== ЗАПУСК =====

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🤖 Бот запущений")
    app.run_polling()

if __name__ == "__main__":
    main()
