import requests
from bs4 import BeautifulSoup
import csv
import re

for page in range(1,30):
    weblink = f'http://books.toscrape.com/catalogue/category/books_1/page-{page}.html'

    req = requests.get(weblink).text

    soup = BeautifulSoup(req , 'lxml')

    print(soup.prettify())
