import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # opts = Options()
    # opts.add_argument("--headless")
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=opts)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def load_url(driver):   
    url = "https://duckduckgo.com/"     
    driver.get(url)
    driver.implicitly_wait(5000)
    yield driver

    

