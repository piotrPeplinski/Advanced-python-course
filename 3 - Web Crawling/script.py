from connect_manager import ConnectToSite
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://books.toscrape.com/index.html'

with ConnectToSite(url) as driver:
    articles = driver.find_elements(By.TAG_NAME,'article')
    links_element = [
        article.find_element(By.TAG_NAME, 'a').get_attribute('href')
        for article in articles
    ]
    print(links_element)
    #link = articles[0].find_element(By.TAG_NAME, 'a')
    #link.click()

    