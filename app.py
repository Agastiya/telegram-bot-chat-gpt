from dotenv import load_dotenv
import telebot
import os
import requests
# -------------------------------------------
# Use this if you have an error about the SSL
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# -------------------------------------------

load_dotenv()

def chatGPT(question):
    api_base = os.environ.get('API_BASE')
    api_key = os.environ.get('API_KEY')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+api_key
    }

    myobj = {
        "model": "pai-001-light",
        "prompt": question,
        "temperature": 0.7,
        "max_tokens": 64,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response = requests.post(api_base, json=myobj, headers=headers)
    resJson = response.json()
    answer = resJson['choices'][0]['text']
    return answer


bot = telebot.TeleBot(os.getenv('TOKEN_TELEGRAM_BOT'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "What can I do for you ?")

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	messageGPT = chatGPT(msg.text)
	bot.reply_to(msg, messageGPT)


print("Bot Start ....")
bot.infinity_polling()
print("Bot Finish")

