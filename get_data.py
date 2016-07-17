# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

def get_xml():
    r = requests.get('http://sntat.ru/rss/yandex_news.xml')
    r.encoding = 'utf-8'
    return r.text

def parse_xml():
    text = get_xml()
    root = ET.fromstring(text)
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


