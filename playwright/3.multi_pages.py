from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 브라우저 실행
    page1 = browser.new_page()
    page1.goto("https://google.com")   
    
    page2 = browser.new_page()
    page2.goto("https://naver.com")     
    
    input("아무키나 누르면 끝납니다")

    browser.close()