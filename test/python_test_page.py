from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.python_pages import PythonPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_page():
    python_page = PythonPage()
    python_page.open_page()
    python_page.search_input().send_keys('Python')
    assert "Python" in python_page.get_page_source()
    python_page.quit_driver()


def try_to_click(xpath_locator: str, waiting_time: int = 5) -> None:
    """Конкретно не сказано какой вид локаторов , поэтому пусть будет по XPATH"""
    python_page = PythonPage()
    python_page.open_page()
    try:
        WebDriverWait(python_page.driver, waiting_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator))
        )
    except TimeoutException:
        print('Элемент не кликается')
    finally:
        python_page.driver.close()





