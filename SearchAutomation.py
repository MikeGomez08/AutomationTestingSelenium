from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Base class for Selenium automation
class SeleniumAutomation:
    def __init__(self, driver_path):
        # Initialize the Chrome driver service
        self.service = Service(driver_path)
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=self.service)
    
    def open_website(self, url):
        # Open the specified URL in the browser
        self.driver.get(url)
        print(f"Opened website: {self.driver.title}")
    
    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Derived class for book search functionality
class BookSearch(SeleniumAutomation):
    def __init__(self, driver_path, url):
        # Initialize the base class
        super().__init__(driver_path)
        # Open the specified URL
        self.open_website(url)
    
    def search_book(self, book_title):
        try:
            # Wait until the search box element is present
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "searchBox"))
            )
            # Enter the book title in the search box
            search_box.send_keys(book_title)
            # Press the RETURN key to submit the search
            search_box.send_keys(Keys.RETURN)
            print(f"Searched for: {book_title}")
            
            # Wait for 5 seconds to observe the results
            time.sleep(5)
        except Exception as e:
            # Print any error that occurs
            print(f"Error: {e}")

# Main block to execute the script
if __name__ == "__main__":
    # Path to the Chrome driver executable
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    # URL of the website to be tested
    URL = "https://demoqa.com/books"
    
    # Create an instance of the BookSearch class
    bot = BookSearch(PATH, URL)
    # Search for a specific book
    bot.search_book("Git Pocket Guide")
    # Close the browser
    bot.close_browser()