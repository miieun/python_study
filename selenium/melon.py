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
    driver.get("https://www.melon.com")
    wait.until(lambda d: d.title !="")
    print(f"title:{driver.title}")

    elem= wait.until(
        EC.visibility_of_element_located((By.ID,"top_search"))
    )
    elem.clear()
    elem.send_keys("bts")
    elem.send_keys(Keys.ENTER)

    # [앨범] 탭으로 이동
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'[title="앨범 - 페이지 이동"]')
        )).click()
    # 첫번째 앨범 선택
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'[title="ARIRANG - 페이지 이동"]')
        )).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH,'//*[@id="frm"]/div/ul/li[1]/div/div/dl/dt/a')
    #     )).click()
    
   
    # 가사 아이콘 클릭
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'[title="Body to Body 곡정보"]')
        )).click()
    # 노래 제목 가져오기
    title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"song_name"))
    ).text
    # 노래 가사 가져오기
    lyric = wait.until(
        EC.visibility_of_element_located((By.ID,"d_video_summary"))
    ).text

    with open(title+".txt", "w", encoding="utf-8") as f:
        f.write(lyric)
    print(f"{title}.txt 파일에 노래가사가 저장되었습니다.")


finally:
    # driver.quit()
    pass