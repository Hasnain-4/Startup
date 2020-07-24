import requests
from bs4 import BeautifulSoup
import csv

req = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text

soup = BeautifulSoup(req , 'lxml')

csv_file = open('newwebsite.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Price' , 'Model' , 'Description', 'Reviews'])

for card in soup.find_all('div', class_= 'col-sm-4 col-lg-4 col-md-4'):


# card1 = card.p
# print(card1)


    card2 = card.find('div', class_='caption')
    # print(card2)

    card3 = card.find('div', class_= 'ratings')
    rat = card3.p.span
    print(rat)

    cardprice = card2.h4.text
    print(cardprice)

    cardanchor = card2.a.text
    print(cardanchor)

    cardpara = card2.p.text
    print(cardpara)

    cardratings = card3.p.text
    print(cardratings)
    print()

    csv_writer.writerow([cardprice,cardanchor,cardpara,cardratings])

# To close the file    
csv_file.close()