# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import os
from newsmaker import * 

bot = telebot.TeleBot(config.token)
day = ''


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Хочешь немного новостей?')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    #markup = types.ForceReply(selective=False)
    message_ = message_maker()
    bot.send_message(message.chat.id, message_)



if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        os.startfile('bot.py')
        print("Here's an ERROR")
