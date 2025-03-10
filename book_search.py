from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base import BaseWebDriver
import config

class BookSearch(BaseWebDriver):
    def __init__(self):
        super().__init__(config.CHROMEDRIVER_PATH)
        self.open_website(config.BASE_URL)

    def search_book(self, book_title):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "searchBox"))
            )
            search_box.send_keys(book_title)
            search_box.send_keys(Keys.RETURN)
            print(f"Searched for: {book_title}")
            time.sleep(5)  # Wait for results
        except Exception as e:
            print(f"Error: {e}")

