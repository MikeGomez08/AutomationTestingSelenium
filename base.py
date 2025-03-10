from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BaseWebDriver:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def open_website(self, url):
        self.driver.get(url)
        print(f"Opened website: {self.driver.title}")

    def close_browser(self):
        self.driver.quit()
