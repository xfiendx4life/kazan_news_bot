from get_data import *

def message_maker():
    news = parse_xml()
    message = 'Главные события на этот час: \n \n'
    for i in range(5):
        message += '%s. %s \n (%s) \n \n' % (i + 1, news[i]['title'], news[i]['link'])
    return message
