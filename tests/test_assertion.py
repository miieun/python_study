from  apps.mycalc import add, subtract, divide
import pytest
import warnings

def test_various_assertion():
    # 참/거짓 검증
    assert True
    assert [1,2,3]
    assert not []
    assert "hello"
    assert not ""
    assert False == 0
    assert True == 1

    # 비교검증
    assert 5 > 3
    assert 10 <= 10
    assert 7 != 8

    # 멤버십 검증
    assert "pytest" in "pytest is easy"
    assert "world" not in "hello universe"
    assert 3 in [1,2,3,4]
    assert 5 not in (1,2,3)

    # 동일성 검증
    a = [1,2]
    b = [1,2]
    c = a 
    assert a == b
    assert a is not b
    assert a is c

# 부동 소수점(float) 비교
def test_float_approx():
    result = divide(1,3)
    assert result == pytest.approx(1/3)  # approx(기대값)
    # assert result == pytest.approx(0.33333)

    # abs 방법(절대오차)
    assert result == pytest.approx(0.33333, abs = 3.4e-6) 

    # rel(상대오차) [실제값 - 예상한값] / 예상한값
    assert result == pytest.approx(0.33333, rel = 1.1e-5)

def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError):  #ZeroDivisionError 발생기대
        divide(10,0)

def test_divide_wrong_type_raises_exception():
    with pytest.raises(ValueError):
        divide(10,2)
    with pytest.raises(ValueError):
        divide(10,"2")


def function_that_warns():
    warnings.warn("이 함수는 곧 제거될 예정입니다", DeprecationWarning)

    return True

def test_deprecation_warning():
    with pytest.warns(DeprecationWarning):
        function_that_warns()

        