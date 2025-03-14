from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumAutomation:
    def __init__(self, driver_path):
        try:
            self.service = Service(driver_path)
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            self.driver = webdriver.Chrome(service=self.service, options=options)
        except Exception as e:
            print(f"Error initializing WebDriver: {e}")
            exit(1)
    
    def open_website(self, url):
        try:
            self.driver.get(url)
            self.handle_ssl_warning()
            print(f"Opened website: {self.driver.title}")
        except Exception as e:
            print(f"Error opening website: {e}")
    
    def handle_ssl_warning(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "details-button"))
            ).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "proceed-link"))
            ).click()
            print("Bypassed SSL warning.")
        except Exception as e:
            print("No SSL warning found or error occurred: ", e)
    
    def click_login_button(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "logintoaccount"))
            )
            login_button.click()
            print("Clicked on 'Log In to your account' button.")

            # Wait for the modal to appear
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "AUTHORIZED"))
            )
            print("Modal appeared successfully.")

            # Click OK button inside the modal
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]") )
            )
            ok_button.click()
            print("Clicked 'OK' button in modal.")
        
        except Exception as e:
            print(f"Error clicking login button or waiting for modal: {e}")
    
    def enter_credentials_and_submit(self, username, password):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "Username"))
            )
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "load"))
            )

            username_field.send_keys(username)
            password_field.send_keys(password)
            submit_button.click()
            print("Entered credentials and clicked submit.")
        except Exception as e:
            print(f"Error entering credentials or clicking submit: {e}")
    
    def select_ppgis_button(self):
        try:
            pp_gis_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "PPGISBTN"))
            )
            pp_gis_button.click()
            print("Clicked on PPGIS button.")
        except Exception as e:
            print(f"Error selecting PPGIS button: {e}")
    
    def click_navbar_button(self):
        try:
            navbar_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/span'))
            )
            navbar_button.click()
            print("Clicked on navbar button.")
        except Exception as e:
            print(f"Error clicking navbar button: {e}")
    
    def click_pole_inventory(self):
        try:
            pole_inventory_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@id="imgdigitize"]'))
            )
            pole_inventory_button.click()
            print("Clicked on Pole Inventory image.")

            generate_ticket_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//li[@id="POLE_INVENTORY"]'))
            )
            generate_ticket_button.click()
            print("Clicked on Generate Ticket.")
        except Exception as e:
            print(f"Error clicking Pole Inventory or Generate Ticket: {e}")
    
    def close_browser(self):
        try:
            input("Press Enter to close the browser...")
            self.driver.quit()
        except Exception as e:
            print(f"Error closing browser: {e}")

class MapPerformanceTest(SeleniumAutomation):
    def __init__(self, driver_path, url):
        super().__init__(driver_path)
        self.open_website(url)
    
    def test_location_performance(self, latitude, longitude):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "searchboxinput"))
            )
            location = f"{latitude}, {longitude}"
            search_box.send_keys(location)
            search_box.send_keys(Keys.RETURN)
            print(f"Searching for location: {location}")
            
            start_time = time.time()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-hero-header-title-title"))
            )
            end_time = time.time()
            print(f"Location loaded in {end_time - start_time:.2f} seconds")
            time.sleep(5)
        except Exception as e:
            print(f"Error during location search: {e}")

if __name__ == "__main__":
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    URL = "https://vptgprprdwapp01/PPGISWEB_EP4_PREBAU/Map/index"
    
    bot = None
    try:
        bot = MapPerformanceTest(PATH, URL)
        bot.click_login_button()
        bot.enter_credentials_and_submit("t-dmdianzon", "p@55w0rd0111")
        bot.select_ppgis_button()
        bot.click_navbar_button()
        bot.click_pole_inventory()
        bot.test_location_performance(14.5562728, 121.0026765)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if bot:
            bot.close_browser()
