from telebot import TeleBot, types

BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False
    )

    keyboard.add(
        types.KeyboardButton("📄 About"),
        types.KeyboardButton("❓ Help")
    )

    bot.send_message(
        message.chat.id,
        "👋 Welcome!\nChoose an option below:",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda m: m.text == "📄 About")
def about(message):
    bot.send_message(
        message.chat.id,
        "This bot uses *Tel*
