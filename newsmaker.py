from get_data import *
from datetime import datetime

def message_maker(): #five recent news
    news = make_news_list()
    message = 'Главные события на этот час: \n \n'
    for i in range(5):
        message += '%s. %s \n (%s) \n \n' % (i + 1, news[i]['title'], news[i]['link'])
    return message

def exchange_rates_message_maker():#making exchange rates message
    try:
        rates = get_ValCurs()
        message = 'Обменный курс на %s по данным Центрального банка cbr.ru: \n\n' % datetime.strftime(datetime.now(),"%d.%m.%Y")
        message += '%s %s = %s RUB \n\n' % (rates[0]['nominal'], rates[0]['name'],
                                       rates[0]['value'])
        message += '%s %s = %s RUB' % (rates[1]['nominal'], rates[1]['name'],
                                       rates[1]['value'])
    except:
        message = 'Что-то пошло не так, попробуйте позже'
    return message
    
def last_news_maker():
    message = ''
    last = check_news()
    if last:
        message += last['title'] + '\n\n' + last['link']
        return message
    return None
