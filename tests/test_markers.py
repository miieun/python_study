import pytest

@pytest.mark.smoke
def test_login():
    print("로그인 기능 테스트")
    assert True

@pytest.mark.regression
def old_bug_case():
    print("예전에 발생했던 버그가 재발하는지 아닌지 확인")
    assert True

@pytest.mark.api
def test_rest_endpoint():
    print("외부 API 호출 테스트")
    assert True

@pytest.mark.slow
def test_big_model_training():
    print("모델학습, 수 분 이상 걸림")
    assert True

@pytest.mark.fast
def test_small_function():
    print("빠르게 끝나는 단위 기능")
    assert True

@pytest.mark.xfail
def test_known_bug():
    assert 1 == 2   # = assert False