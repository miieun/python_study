from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.clear()
    username.send_keys("tomsmith")

    # pwd 입력
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys("SuperSecretPassword!")

    # 로그인 버튼 클릭
    login_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_btn.click()

    # flash msg 가져오기
    flash_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text
    assert "You logged into a secure area!" in flash_msg
    assert "/secure" in driver.current_url