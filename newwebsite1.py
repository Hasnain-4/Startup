import requests
from bs4 import BeautifulSoup
import csv

req = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text

soup = BeautifulSoup(req , 'lxml')
