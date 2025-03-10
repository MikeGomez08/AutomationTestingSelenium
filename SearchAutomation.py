from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumAutomation:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
    
    def open_website(self, url):
        self.driver.get(url)
        print(f"Opened website: {self.driver.title}")
    
    def close_browser(self):
        self.driver.quit()

class BookSearch(SeleniumAutomation):
    def __init__(self, driver_path, url):
        super().__init__(driver_path)
        self.open_website(url)
    
    def search_book(self, book_title):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "searchBox"))
            )
            search_box.send_keys(book_title)
            search_box.send_keys(Keys.RETURN)
            print(f"Searched for: {book_title}")
            
            # Wait to observe results
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    URL = "https://demoqa.com/books"
    
    bot = BookSearch(PATH, URL)
    bot.search_book("Git Pocket Guide")
    bot.close_browser()
