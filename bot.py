import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# 🔐 Токен ТІЛЬКИ з environment
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не знайдено. Перевір Railway → Shared Variables")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["😊 Добре", "😐 Нормально"],
        ["😔 Сумно", "💖 Підтримка"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привіт 💕 Як ти сьогодні?",
        reply_markup=reply_markup,
    )

# Обробка тексту
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "😊 Добре": "Я дуже рада це чути 🥰",
        "😐 Нормально": "Головне — що тримаєшся 💪",
        "😔 Сумно": "Мені шкода 😢 Я поруч",
        "💖 Підтримка": "Ти не одна ❤️ Все буде добре",
    }

    await update.message.reply_text(
        responses.get(text, "Я тебе слухаю 💌")
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот запущений")
    app.run_polling()

if __name__ == "__main__":
    main()
