# fixture 정의
from apps.calculator import Calculator
import pytest

from tests.data_loader import load_test_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def calculator_instance():
    print("\n--Calculator 인스턴스 생성(conftest.py)")
    calc = Calculator()
    return calc

def pytest_generate_tests(metafunc):
    if "ADDCASES" in metafunc.fixturenames:
        cases = load_test_data("add.csv")
        metafunc.parametrize("ADDCASES", cases)
    elif "SUBCASES" in metafunc.fixturenames:
        cases = load_test_data("sub.csv")
        metafunc.parametrize("SUBCASES", cases)
# headless 옵션 등록
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)

#  웹페이지 셀레니움 크롬 드라이버
@pytest.fixture(scope="function")   # 'session'
def driver(request):
    headless = request.config.getoption("--headless")
    opts = Options()
    if headless :
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1280,900")
    d= webdriver.Chrome(options=opts)
    print("###### driver 시작######")
    yield d
    d.quit()

@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.delete_all_cookies()
    driver.get("about:blank")