from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage():
    # url = "https://duckduckgo.com/"
    search_locator = (By.ID, "searchbox_input") # Locator in tuple format

    def __init__(self, driver):
        self.driver = driver

   
    def search(self,phrase):
        search_locator = self.driver.find_element(*self.search_locator)
        search_locator.send_keys(phrase + Keys.RETURN)