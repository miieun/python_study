from pages.login import LoginPage
from selenium import webdriver
import pytest

# 로그인 테스트
def test_login_success(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    flash_msg = page.get_flash_message()

    assert "You logged into a secure area!" in flash_msg
    assert "/secure" in page.current_url()

# 로그아웃 테스트
def test_logout(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    page.click_logout()
    flash_msg = page.get_flash_message()
    
    assert "You logged out of the secure area!" in flash_msg
    assert "/login" in page.current_url()

# 테스트 케이스
LOGIN_CASES = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", "/secure"),
    ("tomsmith", "wrongPwd", "Your password is invalid!", "/login"),
    ("wrongId", "SuperSecretPassword!", "Your username is invalid!", "/login")

]
@pytest.mark.parametrize("username, password, expected_txt, expected_url", LOGIN_CASES)
def test_login(driver, username, password, expected_txt, expected_url):
    page = LoginPage(driver, 10)
    page.open()
    page.login(username, password)
    flash_msg = page.get_flash_message()

    assert expected_txt in flash_msg
    assert expected_url in page.current_url()

