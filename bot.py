import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("8342609349:AAEsYKaV5keWQAWbNWkELJvcYzNgo_eqOzM")

# --- Команди ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["😊 Добре", "😐 Нормально"],
        ["😔 Сумно", "💖 Підтримка"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привіт 💕\nЯ твій милий бот підтримки.\nЯк ти зараз почуваєшся?",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я можу:\n"
        "💬 підтримати тебе\n"
        "😊 запитати про настрій\n"
        "💖 надіслати щось миле\n\n"
        "Просто натисни кнопку ⬇️"
    )

# --- Повідомлення ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "😊 Добре":
        await update.message.reply_text("Я дуже рада це чути! ✨💖")
    elif text == "😐 Нормально":
        await update.message.reply_text("Це теж ок 🌸 Я поруч.")
    elif text == "😔 Сумно":
        await update.message.reply_text("Обіймаю тебе 🤍 Все буде добре.")
    elif text == "💖 Підтримка":
        await update.message.reply_text("Ти неймовірний/неймовірна 💕 Не забувай це.")
    else:
        await update.message.reply_text("Я тебе слухаю 💬")

# --- Запуск ---
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
