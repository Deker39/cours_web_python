import datetime

import requests
import telebot
from telebot import types
from commands import *

TOKEN = '6275499245:AAHa-rKHA63hSKNniqmK65NJ8zdVC3wBRyg'
API_URL = 'https://rickandmortyapi.com/api/'
CHARACTERS = 'character'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=[START])
def send_welcome(message):
    print(message)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton(ALIVE_CH_10.capitalize())
    btn2 = types.KeyboardButton(CH_10.capitalize())
    btn3 = types.KeyboardButton(FILTERS.capitalize())
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, 'hello, choose action', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == CH_10)
def show_latest_movies(message):
    try:
        response = requests.get(API_URL+CHARACTERS).json()
        characters_ten = response['results'][:10]
        print(characters_ten)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'sorry something went wrong')


bot.polling()
