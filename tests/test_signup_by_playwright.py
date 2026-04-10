import pytest
from pages.signup_by_playwright import SignupPage
from playwright.sync_api import expect


SIGNUP_CASES = [
    # (email, username, password, confirm, terms, expected_msg)

    # 정상 가입
    (
        "user@example.com", "tester", "abc12345", "abc12345", True,
        "회원가입이 완료되었습니다",
    ),
    # 이메일 미입력
    (
        "", "tester", "abc12345", "abc12345", True,
        "이메일을 입력해주세요",
    ),
    # 사용자명 미입력
    (
        "user@example.com", "", "abc12345", "abc12345", True,
        "사용자명을 입력해주세요",
    ),
    # 비밀번호 미입력
    (
        "user@example.com", "tester", "", "", True,
        "비밀번호를 입력해주세요",
    ),
    # 비밀번호 불일치
    (
        "user@example.com", "tester", "abc12345", "wrong123", True,
        "비밀번호가 일치하지 않습니다",
    ),
    # 약관 미동의
    (
        "user@example.com", "tester", "abc12345", "abc12345", False,
        "약관에 동의해주세요",
    ),
]


@pytest.mark.parametrize(
    "email, username, password, confirm, terms, expected_msg",
    SIGNUP_CASES,
)
def test_signup(page, email, username, password, confirm, terms, expected_msg):
    sp = SignupPage(page)
    sp.open()
    sp.signup(
        email=email,
        username=username,
        password=password,
        confirm=confirm,
        terms=terms,
    )

    expect(sp.flash).to_contain_text(expected_msg, timeout=5_000)