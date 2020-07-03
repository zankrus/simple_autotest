from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from python_locators.python_locators import PythonPageLocators

PYTHON_URL = 'http://www.ya.ru'


class PythonPage:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def search_input(self):
        driver = self.driver
        elem = driver.find_element(*PythonPageLocators.INPUT_SEARCH)
        return elem

    def open_page(self):
        self.driver.get(PYTHON_URL)

    def quit_driver(self):
        self.driver.quit()

    def get_page_source(self):
        return self.driver.page_source
