"""test case: 
- open url in google crome browser.
- search a word 
- count no. of search links in search page
- check the word is present in search result page."""

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

phrase = "plant"

def test_search_pg(driver):
    serch_pg = DuckDuckGoSearchPage(driver)
    result_pg = DuckDuckGoResultPage(driver)

    serch_pg.load()
    driver.implicitly_wait(5000)
    # print(driver.title )
    # assert "DuckDuckGo" in driver.title 

    serch_pg.search(phrase)
    driver.implicitly_wait(5000)

    # result = result_pg.result()
    # print(result)
    count = 0
    link_title = result_pg.links()
    
    matches = [title for title in link_title if phrase.lower() in title.lower()]
    count = matches.__len__()   
    assert count > 0