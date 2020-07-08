import time

from pages.python_pages import PythonPage


def test_page():
    python_page = PythonPage()
    python_page.open_page()
    python_page.search_input().send_keys('Python')
    python_page.click_search()
    assert "Python" in python_page.get_page_source()
    #python_page.quit_driver()
    python_page.try_to_click('/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/div[2]/button[1]aaaa', 15)
    assert "Python" in python_page.get_page_source()





