import pytest
from tests.data_loader import load_test_data

# @pytest.mark.parametrize("매개변수",[(테스트케이스1),])

add_test_cases = [(2,3,5),(-1,-1,-2),(5,-3,2),(10,0,10),
                  (0.1,0.2,pytest.approx(0.3)),
                  pytest.param(100,200,300, id="large_number")]

@pytest.mark.parametrize("a,b,expected",add_test_cases)
def test_add_cases(calculator_instance,a,b,expected):
    assert calculator_instance.add(a,b) == expected 

# 예외 테스트 
divide_test_cases=[("2",1,TypeError),
                   (10,"2",TypeError),
                   (2,0,ZeroDivisionError),
                   pytest.param(None,2,TypeError,id="None_input")]

@pytest.mark.parametrize("a,b,expected",divide_test_cases)
def test_divide_cases(calculator_instance,a,b,expected):
    # assert calculator_instance.divide(a,b) == expected
    with pytest.raises(expected):
        calculator_instance.divide(a,b)

@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[10,100])
def test_Stacked_cases(x,y):
    assert isinstance(x,int)
    assert isinstance(y,int)

# file 불러오기
@pytest.mark.parametrize("a,b,expected",load_test_data("add.csv"))
def test_add(calculator_instance, a, b, expected):
    if expected == TypeError:
        with pytest.raises(expected):
            calculator_instance.add(a,b)
    else:
        assert calculator_instance.add(a,b) == expected

def test_add2(calculator_instance, ADDCASES):
    a, b, expected = ADDCASES
    if expected == TypeError:
        with pytest.raises(expected):
            calculator_instance.add(a,b)
    else:
        assert calculator_instance.add(a,b) == expected