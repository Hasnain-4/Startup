import requests
from bs4 import BeautifulSoup
import csv
import re

csv_file = open('newwebsite1.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Title' , 'Image Link' , 'Buy Products Page Link' , 'Price' , 'Rating' , 'Stock'])

for page in range(1,50):
    weblink = f'http://books.toscrape.com/catalogue/category/books_1/page-{page}.html'

    req = requests.get(weblink).text

    soup = BeautifulSoup(req , 'lxml')

    # print(soup.prettify())


    for article in soup.find_all('article', class_= 'product_pod'):

    # print(article.prettify())
        try:
            pagelink = article.div.a.get('href')
            pagelink1 = f'http://books.toscrape.com/{pagelink}'
            print(pagelink1)
        except Exception as e:
            pagelink1 = None
        
        try:
            imagelink = article.div.a.img.get('src')
            imagelink1 = f'http://books.toscrape.com/{imagelink}'
            print(imagelink1)
        except Exception as e:
            imagelink1 = None
        
        rating = article.find("p", class_ = re.compile("star-rating")).get("class")[1]
        print(rating)
        # print('http://books.toscrape.com/' + pagelink)
        title = article.h3.a.get('title')
        print(title)

        price = article.find('p', class_= 'price_color').text
        stock = article.find('p', class_= 'instock availability').text
        # price = pricediv.p.get('price_color')
        print(price)
        print(stock)

        print()

    csv_writer.writerow([title , imagelink1 , pagelink1 , price , rating , stock] )

csv_file.close()