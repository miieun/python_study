# fixture 정의
from apps.calculator import Calculator
import pytest

from tests.data_loader import load_test_data

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