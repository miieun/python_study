from apps.calculator import Calculator
import pytest

# @pytest.fixture
# def calculator_instance():
#     calc = Calculator()
#     return calc

def test_add(calculator_instance):
    assert calculator_instance.add(2,3) == 5
    assert calculator_instance.add(-1,1) == 0

def test_subtract(calculator_instance): 
    assert calculator_instance.subtract(2,3) == -1
    assert calculator_instance.subtract(-1,1) == -2

def test_divide(calculator_instance):
    assert calculator_instance.divide(6,3) == 2
    assert calculator_instance.divide(1,3) == pytest.approx(1/3)

def test_divide_by_zero(calculator_instance):
    with pytest.raises(ZeroDivisionError):
        calculator_instance.divide(1,0)