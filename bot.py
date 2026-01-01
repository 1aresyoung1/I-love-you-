from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

TOKEN = "8342609349:AAEsYKaV5keWQAWbNWkELJvcYzNgo_eqOzM"

keyboard = ReplyKeyboardMarkup(
    [
        ["😊 Радісний", "😔 Сумний"],
        ["😴 Втомлений", "😡 Злий"],
        ["😍 Закоханий", "😶 Не знаю"],
        ["💌 Комплімент", "🫂 Обійми"]
    ],
    resize_keyboard=True
)

responses = {
    "😊 Радісний": [
        "Я радий, що ти усміхаєшся 🥰",
        "Твій настрій робить світ яскравішим 💛"
    ],
    "😔 Сумний": [
        "Я поруч 🤍 Ти не одна",
        "Навіть сум пройде, я в тебе вірю 🫂"
    ],
    "😴 Втомлений": [
        "Ти так стараєшся… відпочинь трохи 💕",
        "Навіть супергероям потрібен відпочинок 😴"
    ],
    "😡 Злий": [
        "Злитися — нормально. Я з тобою 🖤",
        "Подихай глибше… все буде добре"
    ],
    "😍 Закоханий": [
        "Це так мило 💖",
        "Нехай це тепло буде з тобою завжди ✨"
    ],
    "😶 Не знаю": [
        "Іноді так буває. І це нормально 🤍"
    ]
}

compliments = [
    "Ти неймовірна 💖",
    "У тебе дуже тепле серце 🥰",
    "Ти робиш цей світ кращим ✨"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт 💕 Як ти сьогодні почуваєшся?",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in responses:
        await update.message.reply_text(random.choice(responses[text]))
    elif text == "💌 Комплімент":
        await update.message.reply_text(random.choice(compliments))
    elif text == "🫂 Обійми":
        await update.message.reply_text("Лови віртуальні обійми 🫂💖")
    else:
        await update.message.reply_text(
            "Я тебе почув 💕 Натисни кнопку або напиши щось від себе",
            reply_markup=keyboard
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
