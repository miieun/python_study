from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    URL = "file:///C:/Users/82107/Documents/swtest/pages/signup.html"

    # Locators
    EMAIL    = (By.ID, "email")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONFIRM  = (By.ID, "confirm")
    TERMS    = (By.ID, "terms")
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH    = (By.ID, "flash")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def clear_and_type(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value or "")

    def signup(self, email="", username="", password="", confirm="", terms=False):
        self.clear_and_type(self.EMAIL, email)
        self.clear_and_type(self.USERNAME, username)
        self.clear_and_type(self.PASSWORD, password)
        self.clear_and_type(self.CONFIRM, confirm)
        self.set_checkbox(self.TERMS, terms)    
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        submit_btn.click()

    def set_checkbox(self, locator, should_be_checked):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        if el.is_selected() != should_be_checked:
            el.click()

    def flash_message(self):
        msg = self.wait.until(
            EC.presence_of_element_located(self.FLASH)
        ).text
        return msg.strip()
    
if __name__ == "__main__":
    options = Options()
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)

    try:
        page = SignupPage(driver)
        page.open()
        page.signup(
            email="user@example.com",
            username="tester",
            password="abc12345",
            confirm="abc12345",
            terms=True
        )
        print("Flash 메시지:", page.flash_message())
    finally:
        driver.quit()
