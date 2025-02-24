from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Program Files (x86)/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/books")
print(driver.title)

search = driver.find_element(By.ID, "searchBox")
search.send_keys("Git Pocket Guide")
search.send_keys(Keys.RETURN)

time.sleep(100000)