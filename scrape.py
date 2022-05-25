#Ankit Sahu
#SRMIST, GE, UTD

from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    # using lxml parser here
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)

print(soup.prettify())

#getting the title of the simple.html
matchTitle = soup.title
matchTitleText = soup.title.text

print(matchTitle)
print(matchTitleText)

#getting the div

matchDiv = soup.div
print(matchDiv)

#getting tag using find method

matchUsingFind = soup.find('div', class_ = 'footer')

print(matchUsingFind)

article = soup.find('div', class_ = 'article')

headline = article.h2.a.text

print(headline)

summary = article.p.text

print(summary)

#find_all method

for article in soup.find_all('div', class_= 'article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()