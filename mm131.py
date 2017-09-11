# -*- coding: utf-8 -*-
# coder:timo

import requests
from bs4 import BeautifulSoup
import re
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')
url = 'http://m.mm131.com'
r= requests.get(url).text
html_doc = r.encode('utf-8')
print html_doc