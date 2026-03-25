from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_experimental_option("detach", True) # 창 계속 켜진 상태
opts.add_argument("--headless=new")   # UI 없이
opts.add_argument("--window-size=1280,900")
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")
    print(f"title:{driver.title}")
finally:
    # driver.quit()
    pass