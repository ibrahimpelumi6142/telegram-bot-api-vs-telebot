from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = "YOUR_BOT_TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("📄 About"), KeyboardButton("❓ Help")]
        ],
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome!\nChoose an option below:",
        reply_markup=keyboard
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "This bot uses *python-telegram-bot* with reply keyboards.",
        parse_mode="Markdown"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use the buttons below to interact with the bot."
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^📄 About$"), about))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^❓ Help$"), help_cmd))

app.run_polling()
