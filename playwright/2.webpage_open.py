from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 브라우저 실행
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")             # 사이트 이동
    print(page.title())                          # 페이지 제목 출력
    page.screenshot(path="screenshot.png")          # 스크린샷 저장


    page.pause()
    context.close()
    browser.close()

