# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import os

def get_xml(url, encoding, payload=""):
    r = requests.get(url, params = payload)
    r.encoding = encoding
    return r.text

def parse_xml(text):
    root = ET.fromstring(text)
    return root


def make_news_list():
    root = parse_xml(get_xml('http://sntat.ru/rss/yandex_news.xml', 'utf-8'))
    news = []
    for child in root[0]:
        if child.tag.split("}")[1] == 'item':
            #print(child[0].tag)
            news_dict = {}
            news_dict['title'] = child.find('{http://backend.userland.com/rss2}title').text
            news_dict['link'] = child.find('{http://backend.userland.com/rss2}link').text
            news_dict['pdalink'] = child.find('{http://backend.userland.com/rss2}pdalink').text
            news_dict['enclosure'] = child.find('{http://backend.userland.com/rss2}enclosure').attrib #check
            news_dict['description'] = child.find('{http://backend.userland.com/rss2}description').text
            news_dict['category'] = child.find('{http://backend.userland.com/rss2}category').text
            #news_dict['yandex:genre'] = child.find('{http://backend.userland.com/rss2}yandex:genre').text
            news_dict['pubDate'] = child.find('{http://backend.userland.com/rss2}pubDate').text
            #news_dict['yandex:full-text'] = child.find('{http://backend.userland.com/rss2}yandex:full-text').text
            news.append(news_dict)
    return news

def get_valCodes(root): #returns list of currency codes from cbr.ru
    code_list = {}
    for item in root:
        if item[1].text == 'US Dollar':
            code_list['US Dollar'] = item.attrib['ID']
        elif item[1].text == 'Euro':
            code_list['EURO'] = item.attrib['ID']
    return code_list
            
def get_rate(day, currency_id, name): #returns rate for one currency, cause u can't get for both at the same time
    url = 'http://www.cbr.ru/scripts/XML_dynamic.asp'
    payload = {'date_req1': day, 'date_req2': day, 'VAL_NM_RQ': currency_id}
    root = parse_xml(get_xml(url,'cp1251', payload))
    rate = {}
    rate['name'] = name
    rate['date'] = root[0].attrib['Date']
    rate['nominal'] = root[0].find('Nominal').text
    rate['value'] = root[0].find('Value').text
    return rate


        
def get_ValCurs(): #returns tuple (us_rate, eu_rate)
    codes = get_valCodes(parse_xml(get_xml('http://www.cbr.ru/scripts/XML_val.asp?d=0',
                                   'cp1251')))
    day = datetime.now()
    if day.weekday() == 6:
        day -= timedelta(days=1)
    day = datetime.strftime(day, "%d.%m.%Y")
    return get_rate(day, codes['US Dollar'],'USD' ), get_rate(day, codes['EURO'], 'EUR')
    
        
def check_news():
    path = os.path.dirname(os.path.realpath(__file__))+ '\\cache.txt'
    with open(path, 'r') as f:
        read_data = f.read()
    last_news  = make_news_list()[0]
    if read_data !=  last_news['link']:
        with open(path, 'w') as f:
            f.write(last_news['link'])
        return last_news
    return None
    
