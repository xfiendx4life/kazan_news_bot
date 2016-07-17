# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_xml(url, encoding):
    r = requests.get(url)
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

def get_valCodes(root):
    code_list = {}
    for item in root:
        if item[1].text == 'US Dollar':
            code_list['US Dollar'] = item.attrib['ID']
        elif item[1].text == 'Euro':
            code_list['EURO'] = item.attrib['ID']
    return code_list
            

def get_ValCurs():
    get_valCodes(parse_xml(get_xml('http://www.cbr.ru/scripts/XML_val.asp?d=0', 'cp1251')))
    
