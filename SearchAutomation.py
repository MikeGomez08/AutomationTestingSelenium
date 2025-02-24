from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Program Files (x86)/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/books")
print(driver.title)

# Wait until the search box is present
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchBox"))
)
search.send_keys("Git Pocket Guide")
search.send_keys(Keys.RETURN)

# Wait for some time to observe the results
time.sleep(10)

driver.quit()
