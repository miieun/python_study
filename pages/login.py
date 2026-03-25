from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    LOGOUT = (By.CSS_SELECTOR, 'a[href="/logout"]')

    def __init__(self, d, timeout = 20):
        self.driver = d
        self.wait = WebDriverWait(d, timeout)

    def open(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        username_input.clear()
        username_input.send_keys(username)

    def input_password(self, pw):
        pw_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        pw_input.clear()
        pw_input.send_keys(pw)

    def click_login(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN)
        )
        login_btn.click()
    
    def login(self, username, pw):
        self.input_username(username)
        self.input_password(pw)
        self.click_login()

    def get_flash_message(self):
        flash_msg = self.wait.until(
        EC.visibility_of_element_located(self.FLASH)
        ).text
        return flash_msg
    
    def click_logout(self):
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT)
        )
        logout_btn.click()

    def current_url(self):
        return self.driver.current_url
    
# LoginPage 클래스가 잘 동작하는지 확인
if __name__ == "__main__":
    d = webdriver.Chrome()
    page = LoginPage(d, 10)
    page.open()
    page.login("tomsmith","SuperSecretPassword!")
    # print(d.title)
    print(page.get_flash_message())
    print(page.current_url())
    # input("키를 눌러야 종료됩니다") #창 유지
    # time.sleep(10)

