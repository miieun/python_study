# Python Study for QA Automation

Python 기초 문법부터 pytest 기반 테스트 자동화, Selenium · Playwright 웹 자동화까지  
QA 자동화와 연결되는 테스트 코드 작성 방식을 학습한 저장소입니다.

---

## 학습 목적

- pytest를 활용한 단위 테스트 작성 (assertion, fixture, parametrize, marker)
- CSV 기반 테스트 데이터 로딩 및 동적 파라미터화
- Selenium · Playwright를 활용한 웹 UI 자동화
- Page Object Model 패턴 적용
- QA 자동화 학습 기반 만들기

---

## 저장소 구성

**`apps/`** — 테스트 대상 애플리케이션
- `mycalc.py` : add / subtract / divide 함수, 타입 검증, 예외 처리
- `calculator.py` : Calculator 클래스 기반 구현

**`tests/`** — pytest 테스트 코드
- `test_assertion.py` : truthy/falsy, 비교, 멤버십, pytest.approx, pytest.raises, pytest.warns
- `test_calculator.py` : fixture 활용, 부동소수점 비교, 예외 테스트
- `test_calculator_param.py` : parametrize, 스택 parametrize, CSV 데이터 로딩
- `test_fixture_scope.py` : fixture scope (function / class / session)
- `test_fixture_yield.py` : yield fixture로 setup / teardown 구현
- `test_markers.py` : 커스텀 marker (smoke, regression, api, slow, xfail)
- `test_login.py` / `test_signup.py` : Selenium 로그인 · 회원가입 자동화
- `test_login_by_playwright.py` : Playwright + parametrize 로그인 정상/예외 검증, Page Object Model 적용
- `test_dynamic_loading_by_playwright.py` : 동적 로딩 요소 대기 처리 5가지 방법 비교
- `conftest.py` : calculator / driver / browser / page fixture 공유 설정

**`playwright/`** — Playwright 기초 실습
- 브라우저 실행, 페이지 이동, 스크린샷 저장
- 멀티 페이지 동시 제어 (Google + Naver)

**`selenium/`** — Selenium 기초 실습
- 페이지 이동, 요소 탐색, 명시적 대기 (WebDriverWait)

---


## 사용 기술

`Python` `pytest` `Selenium` `Playwright` `Page Object Model`
