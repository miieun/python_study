from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts = Options()
opts.add_experimental_option("detach", True) # 창 계속 켜진 상태
# opts.add_argument("--headless=new")   # UI 없이
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.python.org")
    wait.until(lambda d: d.title !="")  # 타이틀 빌 때까지 대기
    print(f"title:{driver.title}")

    # elem = driver.find_element(By.ID,"id-search-field")
    elem= wait.until(
        EC.visibility_of_element_located((By.ID,"id-search-field")))   #요소 보일때까지 대기
    elem.clear()
    elem.send_keys("list")
    elem.send_keys(Keys.ENTER)
    
    # 검색 후, Search Python.org가 나올 때까지 기다림
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "h2"), "Search Python.org")
    )
finally:
    # driver.quit()
    pass