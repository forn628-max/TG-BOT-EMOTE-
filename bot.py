import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

bot = telebot.TeleBot("8234200983:AAH5bas9W6WZPfAS1mdC_EvSwfL2b0QC3PM")

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🎮 OPEN MINI APP", web_app=WebAppInfo("https://bot-web-9ugn.onrender.com"))
    markup.add(btn)
    bot.send_message(message.chat.id, """
⚡ *Send Emotes to your Targets* ✨

*Features You'll Love:*
⚡ Send Emotes: With Just One Click
🎁 Send Emotes: 100% Free
⭐ Sends Emotes: Instantly
♾️ Sends: Unlimited Emotes
✅ 1000% Safe To Use ✅

👇 *Click Below to Open - Enjoy the Mini App!*
    """, parse_mode='Markdown', reply_markup=markup)

@app.route('/')
def home():
    return "Bot is running! 🚀"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    bot_thread = Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
