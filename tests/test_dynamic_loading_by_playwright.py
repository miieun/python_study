
from playwright.sync_api import sync_playwright, Page, expect


URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

def test_dynamic_loading_playwright(page:Page):
    page.goto(URL)
    page.locator("#start button").click()

    # [방법1]
    # flash_msg = page.locator("#finish").inner_text()
    # print(f"####{flash_msg}####")
    # assert "Hello World!" in flash_msg

    # [방법2]
    # flash = page.locator("#finish")
    # expect(flash).to_have_text("Hello World!", timeout=10000) #, timeout=100

    # [방법3]
    # expect(page.locator("loading")).to_be_hidden(timeout=10000)
    # flash = page.locator("#finish")
    # expect(flash).to_have_text("Hello World!", timeout=10000)

    # [방법4]
    # flash = page.locator("#finish")
    # expect(flash).to_have_text("Hello World!", use_inner_text=True, timeout=10000)
    # page.pause()
    
    # [방법5]
    flash = page.get_by_role("heading", name="Hello World!")
    expect(flash).to_have_text("Hello World!", timeout=10000)
    
