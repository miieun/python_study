# tests/test_mycalc.py
from apps.mycalc import add, subtract
import pytest

def test_add_positive_number():
    a = 12
    b = 13
    expect = 25

    actual = add(a,b)

    assert expect == actual

def test_add_negative_number():
    a = -3
    b = -8
    expect = -11

    actual = add(a,b)

    assert expect == actual


# 미션 subtract()
def test_subtract_positive_number():
    assert subtract(10,3) == 7

def test_subtract_negative_result():
    assert subtract(5,8) == -3

def test_subtract_with_negative_number():
    assert subtract(5,-3) == 8
    assert subtract(-3,5) == -8

# def test_fail_example():
#     assert add(1,1) == 3
