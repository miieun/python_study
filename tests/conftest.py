# fixture 정의
from apps.calculator import Calculator
import pytest

@pytest.fixture(scope="class")
def calculator_instance():
    print("\n--Calculator 인스턴스 생성(conftest.py)")
    calc = Calculator()
    return calc