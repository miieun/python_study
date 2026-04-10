from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    #   chromium 브라우저 열기 (headless=False: 화면에 표시)
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # 구글 페이지 이동
    page.goto('https://www.google.com')

    # 페이지 제목 출력
    title = page.title()
    print(f'페이지 제목: {title}')

    # 3초 대기 후 브라우저 닫기
    page.wait_for_timeout(3000)
    browser.close()
    print('브라우저 종료 완료!')