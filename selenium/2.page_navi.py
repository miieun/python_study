import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_experimental_option("detach", True) # 창 계속 켜진 상태
# opts.add_argument("--headless=new")   # UI 없이
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title:{driver.title}")

    time.sleep(3)
    driver.get("https://www.naver.com")
    print(f"title:{driver.title}")
    time.sleep(3)

    # page backward, forward, 새로고침
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.refresh()


finally:
    # driver.quit()
    pass