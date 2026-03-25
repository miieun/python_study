from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_experimental_option("detach", True) # 창 계속 켜진 상태
# opts.add_argument("--headless=new")   # UI 없이
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title:{driver.title}")

    elem = driver.find_element(By.ID,"id-search-field")
    elem.clear()
    elem.send_keys("list")
    elem.send_keys(Keys.ENTER)
    
finally:
    # driver.quit()
    pass