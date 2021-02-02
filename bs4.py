# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml

req = requests.get("http://example.com/")
html = req.content
soup = BeautifulSoup(html, 'lxml')
content = soup.find_all("div", {"class": "a"})

print(content)
