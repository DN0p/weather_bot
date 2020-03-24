import telebot
from telebot import apihelper
from weather_api import *

apihelper.proxy = {'https':'socks5://v3_178771112:DUbZPXCw@s5.priv.opennetwork.cc:1080'}
bot = telebot.TeleBot('Enter your key here')
print(bot.get_me())


@bot.message_handler(commands=['start'])
def start_message(mess):
    bot.send_message(mess.chat.id, 'Привет, сейчас я помогу тебе одеться. Введи свой город')


@ bot.message_handler(content_types='text')
def send_text(mess):
    if mess.text.lower() == 'стикер':
        bot.send_sticker(mess.chat.id, 'CAADAgADDQADr8ZRGj7pvDy3DEgWFgQ')
    else:
        bot.send_message(mess.chat.id, weather(mess.text))


bot.polling(timeout=5)

