#!/usr/bin/env python  
# encoding: utf-8   
""" 
@Author:timo
time:20170907
"""
import requests
import re
from bs4 import BeautifulSoup
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

site = 'http://www.ind-building.com'
urls = ['http://www.ind-building.com/Index/news/id/1/p/{}.html'.format(str(i)) for i in range(1, 70, 1)]

for url in urls:
    get_url = requests.get(url)
    get_url_soup = BeautifulSoup(get_url.text, 'lxml')
    news_urls = get_url_soup.select("ul > a")
    for news_url in news_urls:
        new_url = site + news_url.get('href')

    NewsPages = requests.get(new_url)
    NewsPages_soup = BeautifulSoup(NewsPages.text, 'lxml')
    titlee = NewsPages_soup.find("div", class_="info_t")
    title = titlee.find("h2").get_text()
    content = NewsPages_soup.find("div", "mat-dtext").get_text()
    News = title + content
    localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print title
    print localTime
    filename = "E:\\python project\\1\\"+localTime+".txt"
    file = open(filename,'w')
    file.write(News)
    file.close()
    time.sleep(1)