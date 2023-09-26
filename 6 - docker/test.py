import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

articles = soup.find_all('article')

titles = []
prices = []


for article in articles:
    title = article.find_all('a')[1].attrs['title']
    price = article.find(class_='price_color').text[2:]
    titles.append(title)
    prices.append(price)

df = pd.DataFrame({
    'Title': titles,
    'Price':prices
})
print(df)
   