#Ankit Sahu
#SRMIST, GE, UTD

from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    # using lxml parser here
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)

print(soup.prettify())