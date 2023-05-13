import datetime

import random
import telebot
from telebot import types
from commands import *

TOKEN_TELEGRAM_BOT = '6275499245:AAHa-rKHA63hSKNniqmK65NJ8zdVC3wBRyg'

bot = telebot.TeleBot(TOKEN_TELEGRAM_BOT)
writers = ['Leo Tolstoy', 'William Shakespear', 'James Joyce ', 'Vladimir Nabokov', 'Fyodor Dostoevsky',
           'William Faulkner', 'Charles Dickens', 'Anton Chekhov']
poets = ['William Shakespeare', 'Sylvia Plath', 'Ted Hughes', 'Dante Alighieri', 'Maya Angelou', 'Sappho',
         'Lord Byron', 'Li Bai']
books = ['Anna Karenina', 'Madame Bovary', 'War and Peace', 'The Great Gatsby', 'Lolita', 'Middlemarch',
         'The Adventures of Huckleberry Finn', 'The Stories of Anton Chekhov', 'In Search of Lost Time', 'Hamlet']
monologue = ['Taken', 'Everything Everywhere All At Once', ' Call Me By Your Name',
             'The Lord of the Rings: The Two Towers', 'The Great Gatsby', 'American Psycho', 'Queen & Slim',
             'Star Wars Episode V', 'Whiplash', 'Whiplash']


@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, 'Hello, to the hw88')


@bot.message_handler(content_types=['text'])
def answer_user(message):
    if message.text.lower() == 'writer':
        bot.send_message(message.chat.id, writers[random.randint(0, len(writers))])
    elif message.text.lower() == 'poet':
        bot.send_message(message.chat.id, poets[random.randint(0, len(writers))])
    elif message.text.lower() == 'book':
        bot.send_message(message.chat.id, books[random.randint(0, len(writers))])
    elif message.text.lower() == 'monologue':
        bot.send_message(message.chat.id, monologue[random.randint(0, len(writers))])

bot.polling()

