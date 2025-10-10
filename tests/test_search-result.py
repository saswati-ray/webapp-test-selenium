"""
test case: 
- open url in google crome browser.
- search a word 
- count no. of search links in search page
- check the word is present in search result page.
"""

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

phrase = "plant"

# verify DuckDuckGo is there in Home page title
def test_title_verify(load_url):
    driver = load_url
    assert "DuckDuckGo" in driver.title 

# verify search box present
def test_searchbox_verify(load_url):
    driver = load_url
    serch_pg = DuckDuckGoSearchPage(driver)
    search_box = serch_pg.driver.find_element(*serch_pg.search_locator)
    assert search_box.is_displayed()

# Fter search a word verify that word present in result links  
def test_result_pg(load_url):
    driver = load_url
    serch_pg = DuckDuckGoSearchPage(driver)
    serch_pg.search(phrase)
    driver.implicitly_wait(5000)

    result_pg = DuckDuckGoResultPage(driver)
    result = result_pg.result()
    print(result)

    count = 0
    link_title = result_pg.links()
    
    matches = [title for title in link_title if phrase.lower() in title.lower()]
    count = matches.__len__()   
    assert count > 0