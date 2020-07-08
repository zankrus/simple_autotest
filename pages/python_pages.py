from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from python_locators.python_locators import PythonPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PYTHON_URL = 'http://www.ya.ru'


class PythonPage:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def search_input(self):
        driver = self.driver
        elem = driver.find_element(*PythonPageLocators.INPUT_SEARCH)
        return elem

    def click_search(self):
        driver = self.driver
        driver.find_element(*PythonPageLocators.SEARCH_BUTTON).click()

    def open_page(self):
        self.driver.get(PYTHON_URL)

    def quit_driver(self):
        self.driver.quit()

    def get_page_source(self):

        return self.driver.page_source

    def try_to_click(self,xpath_locator: str, waiting_time: int = 5) -> None:
        """Конкретно не сказано какой вид локаторов , поэтому пусть будет по XPATH"""
        python_page = PythonPage()
        python_page.open_page()
        try:
            WebDriverWait(python_page.driver, waiting_time).until(
                EC.element_to_be_clickable((By.XPATH, xpath_locator))
            )
            python_page.driver.find_element_by_xpath(xpath_locator).click()
        except TimeoutException:
            print('Элемент не кликается')
        finally:
            python_page.driver.close()

