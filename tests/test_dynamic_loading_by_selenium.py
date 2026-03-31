# tests/test_dynamic_loading_by_selenium.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

def test_dynamic_loading_selenium(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(URL)
    # driver.find_element(By.CSS_SELECTOR, "#start button")
    wait.until(
        EC.element_to_be_clickable(   
            (By.CSS_SELECTOR, "#start button") )
    ).click()

    #driver.find_element(By.ID, "finish")
    flash_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    ).text

    assert "Hello World!" in flash_msg

    
