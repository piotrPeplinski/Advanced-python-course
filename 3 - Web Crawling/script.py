import requests
from bs4 import BeautifulSoup
import json

with open('links.json') as file:
    links = json.load(file)


r = requests.get(links[0])

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('h1')

print(title.text)
