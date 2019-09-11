# Use the BeautifulSoup and requests Python packages
# print out a list of all the article titles on the BBC homepage

# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.co.uk/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
title = soup.findAll(class_="top-story__title")

for item in title:
    print(item.text.strip()+"\n")
