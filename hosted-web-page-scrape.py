#Ankit Sahu
#SRMIST, GE, UTD

from bs4 import BeautifulSoup
import requests

source =  requests.get('https://coreyms.com').text
# print(source)
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
for article in soup.find_all('article'):
    headline = article.h2.a.text
    # print(headline)

    # summary = article.find('div', class_ = 'entry-content').p.text

    # print(summary)
    if article is not None:
        ytspan = article.find('span', class_='embed-youtube')

# print(ytspan.prettify())
    if ytspan is not None:
        ytID = ytspan.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
    if ytID is not None:
        yt_link = f'https://youtube.com/watch?v={ytID}'
        print(headline + " " + yt_link)