from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page1 = context.new_page()
    page1.goto("https://google.com")   
    
    page2 = context.new_page()
    page2.goto("https://naver.com")     
    
    input("아무키나 누르면 끝납니다")
    context.close()
    browser.close()