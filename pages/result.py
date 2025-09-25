from selenium.webdriver.common.by import By

class DuckDuckGoResultPage():
    search_locator = (By.ID, "search_form_input") # Locator in tuple format
    link_locator = (By.XPATH, ".//div/h2/a/span")

    def __init__(self, driver):
        self.driver = driver

    def result(self):
        search_locator = self.driver.find_element(*self.search_locator)
        return search_locator.get_attribute('value')

    def links(self):
        links = self.driver.find_elements(*self.link_locator)
        title = [link.text for link in links]
        return title
