import requests
from bs4 import BeautifulSoup
import json

rating_enum = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

with open('links.json') as file:
    links = json.load(file)


r = requests.get(links[0])

soup = BeautifulSoup(r.text, 'html.parser')

stock_el = soup.find(class_='availability').stripped_strings
rating_key = soup.find(class_='star-rating').attrs['class'][1]

title = soup.find('h1').text
price = soup.find(class_='price_color').text[2:]
stock = list(stock_el)[0].split(' ')[2][1:]
rating = rating_enum[rating_key]

