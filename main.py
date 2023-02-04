import telebot
from chatGPT import chatGPT

bot = telebot.TeleBot("5636924719:AAG2linASVMzsiT0Ov-z_EVkmkvdeS5peM8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Selamat datang di bot chatGPT")

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	messageGPT = chatGPT(msg.text)
	bot.reply_to(msg, messageGPT)


print("Bot Start ....")
bot.infinity_polling()
print("Bot Finish")

