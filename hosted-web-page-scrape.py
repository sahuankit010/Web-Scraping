#Ankit Sahu
#SRMIST, GE, UTD

from bs4 import BeautifulSoup
import requests
import csv

source =  requests.get('https://coreyms.com').text
# print(source)
soup = BeautifulSoup(source, 'lxml')
#writing to a file here
csv_file = open('cms.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# print(soup.prettify())
for article in soup.find_all('article'):
    headline = article.h2.a.text
    # print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text

    # print(summary)
    if article is not None:
        ytspan = article.find('span', class_='embed-youtube')

# print(ytspan.prettify())
    if ytspan is not None:
        ytID = ytspan.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
    if ytID is not None:
        yt_link = f'https://youtube.com/watch?v={ytID}'
        print(headline + " " + yt_link)
        csv_writer.writerow([headline,summary,yt_link])


csv_file.close()        