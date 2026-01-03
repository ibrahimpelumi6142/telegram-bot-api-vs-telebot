from telebot import TeleBot

bot = TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Hello! This bot is built using TeleBot.\nType /help to continue."
    )

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.send_message(
        message.chat.id,
        "Available commands:\n/start\n/help"
    )

bot.infinity_polling()
