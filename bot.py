import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Беремо токен з Railway Variables
TOKEN = os.getenv("8342609349:AAHpFcc-mY735PX4D6w5pjQLIncJP1bbeyA")

# --- Команда /start ---
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
        "Привіт! 💕\nЯк ти себе почуваєш сьогодні?",
        reply_markup=reply_markup
    )

# --- Обробка кнопок ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "😊 Добре": "Я дуже рада це чути! ✨",
        "😐 Нормально": "Це теж нормально 💛",
        "😔 Сумно": "Мені шкода 😔 Я поруч.",
        "💖 Підтримка": "Ти не одна 💕 Все буде добре."
    }

    await update.message.reply_text(
        responses.get(text, "Я тебе чую 💫")
    )

# --- Запуск бота ---
def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не знайдено. Додай його в Railway Variables.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот запущений")
    app.run_polling()

if __name__ == "__main__":
    main()
