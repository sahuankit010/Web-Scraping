#Ankit Sahu
#SRMIST, GE, UTD

from bs4 import BeautifulSoup
import requests

source =  requests.get('https://coreyms.com').text
# print(source)
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')

headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_ = 'entry-content').p.text

# print(summary)

ytspan = article.find('span', class_='embed-youtube')

# print(ytspan.prettify())

ytID = ytspan.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]

yt_link = f'https://youtube.com/watch?v={ytID}'
print(yt_link)