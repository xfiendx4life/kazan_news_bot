# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import os
from newsmaker import * 

bot = telebot.TeleBot(config.token)
day = ''
cat = False

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Хочешь немного новостей?')

@bot.message_handler(commands=['category'])
def handle_cat(message):
    cat_list = get_cat(make_news_list())
    markup = types.ReplyKeyboardMarkup(row_width = 1)
    itembtn = 0
    print(cat_list)
    for item in cat_list:
        itembtn = types.KeyboardButton(item)
        markup.add(itembtn)
    global cat
    cat = True
    bot.send_message(message.chat.id, 'Выберите категорию' ,reply_markup=markup)
    
@bot.message_handler(commands=['news'])
def handle_news(message):
    markup = types.ReplyKeyboardHide(selective=False)
    message_ = message_maker()
    bot.send_message(message.chat.id, message_, reply_markup=markup)
    #print(message)


@bot.message_handler(commands=['exchangerate'])
def handle_exchangerates(message):
    message_ = exchange_rates_message_maker()
    bot.send_message(message.chat.id, message_)

@bot.message_handler(func=lambda message: True)
def handle_plain_text(message):
    markup = types.ReplyKeyboardHide(selective=False)
    global cat
    if cat:
        category = message.text
        message_ = cat_news_maker(category)
        bot.send_message(message.chat.id, message_, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Чтобы узнать новости, пользуйтесь командами'
                         ' /news или /exchangerate для курса валют. Если вас интересует '
                         'определенная категория выбирайте /category', reply_markup=markup)
    cat = False

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        os.startfile('bot.py')
        print("Here's an ERROR")
