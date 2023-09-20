from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ConnectToSite:
    def __init__(self, url: str):
        self.__url = url

    def __enter__(self):
        self.__driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.__driver.get(self.__url)
        # proxy
        return self.__driver

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.__driver.quit()
