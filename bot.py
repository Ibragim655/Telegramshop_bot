from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7560893066:AAHJ6_BUDL9rQCC3La51bQ8aIPt12q3JLi0"

products = {
    'куртка': 'https://сайт.ком/картинка_куртки.jpg',
    'рубашка': 'https://сайт.ком/картинка_рубашки.jpg',
    'штаны': 'https://сайт.ком/картинка_штанов.jpg'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши название товара (например: куртка, рубашка)")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in products:
        await update.message.reply_photo(products[text])
    else:
        await update.message.reply_text("Товар не найден. Попробуй: " + ", ".join(products.keys()))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен")
app.run_polling()
