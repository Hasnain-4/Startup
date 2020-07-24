from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source , 'lxml')

# print(soup.prettify())
csv_file = open('first_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Heading', 'Summary' , 'Youtube link'])

for article in soup.find_all('article'):


    paras = article.find('div', class_ = 'entry-content').p.text
    print(paras)
    print()
    anchor = article.a.text

    #print(article.prettify())
    print(anchor)
    print()
    try:
        
        video = article.find('iframe' , class_ = 'youtube-player')['src']

        video_id = video.split('/')[4]

        vid_id = video_id.split('?')[0]
        
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e :
        yt_link = None

    #print('https://youtube.com/watch?v=' +vid_id)

    print(yt_link)
    print( )

    csv_writer.writerow([anchor , paras , yt_link])

csv_file.close()


