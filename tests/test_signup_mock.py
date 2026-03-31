import pytest
import json
from pages.signup_by_playwright import SignupPage
from playwright.sync_api import expect

URL = "file:///C:/Users/82107/Documents/swtest/pages/signup_mock.html"

FAKE_CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status":"ok", "message":"회원가입 성공(Mocked)"},
        "expected": "회원가입 성공(Mocked)"
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status":"error", "message":"서버 오류(Mocked)"},
        "expected": "서버 오류(Mocked)"
    },
]
@pytest.mark.parametrize("case", FAKE_CASES, ids=[i["id"] for i in FAKE_CASES])
def test_signup_mock(page, case):
    def handle_mock_response(route):
        route.fulfill(
            status = case["status"],
            content_type = "application/json",
            body = json.dumps(case["json_body"])
        )
    page.route("http://localhost:8000/api/signup", handle_mock_response)


    s = SignupPage(page)
    s.open(URL)
    s.signup(
        email= "test@ex.com",
        username= "honggildong",
        password= "abc12345",
        confirm= "abc12345",
        terms=True
    )

    print(f"###mock test : {s.get_flash_msg()}")
    expect(s.flash).to_contain_text(case["expected"])
