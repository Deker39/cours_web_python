import datetime

import requests
import telebot
from telebot import types
from commands import *

TOKEN_TELEGRAM_BOT = '6275499245:AAHa-rKHA63hSKNniqmK65NJ8zdVC3wBRyg'
TOKEN_API_RANDOM = 'b5348ba2-55f1-479c-b912-f437ecfc4e8a'

bot = telebot.TeleBot(TOKEN_TELEGRAM_BOT)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello, to the random world')
    bot.send_message(message.chat.id, 'Please, write a three params for random test:\n'
                                      'Min value, Max value, Number of values\n'
                                      'Example: 10, 20, 5')


@bot.message_handler(content_types=['text'])
def answer_user(message):
    # list(map(int, kek.replace(' ', '').split(',')))
    answ_us = message.text.replace(' ', '').split(',')
    if len(answ_us) == 3:
        incorrect_format = [i for i in answ_us if not i.isdigit()]
        if len(incorrect_format) > 0:
            bot.send_message(message.chat.id, f'Incorrect format,invalid format, one or several of the parameters '
                                              f'is not a number: {", ".join(incorrect_format)}')
        else:

            start_range, end_range, numb = answ_us
            url = f'https://www.random.org/integers/?num={numb}&min={start_range}&max={end_range}&col=1&base=10&format=plain&rnd=new'
            x = requests.get(url)
            bot.send_message(message.chat.id, 'Yor parameters:\n'
                                              f'min value: {start_range}\n'
                                              f'max value: {end_range}\n'
                                              f'number of values: {numb}\n'
                                              f'{x.text}' if x.text.isdigit() else f'{x.text}')


    else:
        bot.send_message(message.chat.id, f'The number of parameters does not match 3, please try again')



                                      

bot.polling()

