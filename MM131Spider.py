#!/usr/bin/env python  
# encoding: utf-8   
""" 
@Author:timo
time:#170922
"""
import requests
from bs4 import BeautifulSoup
import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
site = 'http://m.mm131.com'
urls = ['http://m.mm131.com/more.php?page={}'.format(str(i)) for i in range(1, 50, 1)]
path = 'E:\\spiderprojects\\mm131\\'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}

'''主题列表获取'''

for url in urls:
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    picc_urls = soup.find_all("a", class_="post-title-link")
    for picc_url in picc_urls:
        pic_urls = site + picc_url.get('href')
        #单主题图片数量获取
        pic_html = requests.get(pic_urls)
        pic_html.encoding='gb2312'
        pic_soup = BeautifulSoup(pic_html.text,'lxml')
        max_num = pic_soup.find_all("span",class_="rw")
        pic_max_num = max_num[0].text[2:-1] #数量获取完毕
        pic_series = picc_url.get('href')[9:13]
        pic_title = pic_soup.find("h2",class_="mm-title").text.strip()
        if (os.path.exists(path + pic_title)):
            print('目录已存在')
        else:
            os.makedirs(path + pic_title)
            print ('新建目录中'+pic_title)
        os.chdir(path + pic_title)
        for num in range(1, int(pic_max_num) + 1):
            img_name = '%s.jpg' % (num)
            img_src = 'http://img1.mm131.com/pic/%s/%s.jpg'%(pic_series,num)
            print img_src
            img_src_html = requests.get(img_src)
            f = open(img_name,'wb')
            f.write(img_src_html.content)
            f.close()
            print ('got it',num)
            time.sleep(1)
