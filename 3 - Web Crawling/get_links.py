from connect_manager import ConnectToSite
from selenium.webdriver.common.by import By
from time import sleep
import json


url = 'http://books.toscrape.com/index.html'

with ConnectToSite(url) as driver:
    articles = driver.find_elements(By.TAG_NAME, 'article')
    links = [
        article.find_element(By.TAG_NAME, 'a').get_attribute('href')
        for article in articles
    ]

with open('links.json', 'w') as file:
    json.dump(links, file)
