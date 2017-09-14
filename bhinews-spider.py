#!/usr/bin/env python  
# encoding: utf-8   
""" 
@Author:timo
time:#20170914
"""
import requests
from bs4 import BeautifulSoup
import json
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

site = 'http://www.bhi.com.cn'
urls = [
    'http://www.bhi.com.cn/NavigationPage/solr_infomation.ashx?solr_core=0&solr_rows=50&solr_rsort=0&solr_keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&solr_area=&solr_industry=&solr_date=0&solr_cbcolumns=%E6%8A%95%E8%B5%84,%E6%94%BF%E7%AD%96,%E8%A1%8C%E4%B8%9A,%E7%BB%8F%E6%B5%8E%E8%A6%81%E9%97%BB,&solr_currentPage={}&_=1505365718888'.format(
        str(i)) for i in range(1, 40, 1)]

for url in urls:
    r = requests.get(url)
    r.encoding = 'utf-8'
    r_json = r.json()
    docs = r_json['docs']
    for doc in docs:
        title = doc['title']
        soup = BeautifulSoup(title, 'lxml')
        links = soup.find_all('a')
        for link in links:
            newslink = site + link.get('href')
            news_page = requests.get(newslink)
            news_soup = BeautifulSoup(news_page.text, 'lxml')
            news_title = news_soup.find("p", class_="titlestyle").get_text().strip()
            news_text = news_soup.find("div", class_="contentstyle contentstyle1")
            filename = "E:\\spiderprojects\\bhi-news\\" + news_title + ".txt"
            f = open(filename, 'w')
            f.write("标题："+str(news_title[0:10])+
                    "内容："+str(news_text))
            f.close()
            time.sleep(1)
