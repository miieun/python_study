# Python Study for QA Automation

Python 기초 문법, pytest 기반 테스트 자동화, CSV 데이터 기반 테스트, Selenium 기초 실습을 정리한 학습 저장소입니다.

단순 문법 학습에 그치지 않고, QA 자동화와 연결될 수 있는 테스트 코드 작성 방식과 fixture, parameterize, 예외 처리, Selenium 웹 자동화 기초까지 함께 연습했습니다.

---

## 학습 목적

- Python 기초 문법 익히기
- 함수와 클래스 기반 로직 구현 연습
- pytest를 활용한 단위 테스트 작성
- CSV 기반 테스트 데이터 로딩 실습
- fixture / yield / scope 개념 이해
- Selenium을 활용한 웹 자동화 기초 학습
- QA 자동화 학습 기반 만들기

---

## 저장소 구성

### `apps/`
간단한 계산기 로직을 함수형 / 클래스형으로 구현한 코드가 포함되어 있습니다.

- `mycalc.py`
  - `add`, `subtract`, `divide` 함수 구현
  - 숫자 타입 검증
  - 0으로 나누기 예외 처리

- `calculator.py`
  - `Calculator` 클래스로 계산 기능 구현
  - 타입 검증 및 예외 처리 포함

---

### `tests/`
pytest를 사용한 테스트 코드가 포함되어 있습니다.

- `test_calculator.py`
  - fixture를 활용한 `Calculator` 인스턴스 테스트
  - add / subtract / divide 검증
  - `pytest.approx`를 사용한 부동소수점 비교
  - `ZeroDivisionError` 예외 테스트

- `test_calculator_param.py`
  - `pytest.mark.parametrize` 기반 다중 테스트
  - 예외 테스트
  - stacked parameterize 예제
  - CSV 파일 기반 테스트 데이터 로딩

- `test_assertion.py`
  - 다양한 assertion 문법 학습
  - truthy / falsy / 비교 / 멤버십 / 동일성 검증
  - `pytest.approx`, `pytest.raises`, `pytest.warns` 예제

- `test_fixture_scope.py`
  - fixture의 `scope="class"` 학습

- `test_fixture_yield.py`
  - `yield fixture`를 활용한 파일 열기/닫기 실습

- `data_loader.py`
  - CSV 파일을 읽어 테스트케이스를 로드하는 함수 구현
  - `csv.DictReader`, `ast.literal_eval`, `Path` 활용

- `conftest.py`
  - 공통 fixture 정의
  - `calculator_instance` fixture
  - `pytest_generate_tests`를 통한 동적 파라미터화
  - Selenium용 `driver` fixture와 브라우저 초기화 fixture 포함

---

### `selenium/`
Selenium을 사용한 웹 자동화 기초 예제가 포함되어 있습니다.

- `1.webpage_open.py`
  - Python.org 접속 및 페이지 title 확인

- `2.page_navi.py`
  - 페이지 이동, 뒤로가기, 앞으로가기, 새로고침

- `3.find_elem.py`
  - 검색창 요소 찾기 및 키 입력

- `4.wait.py`
  - `WebDriverWait`와 `expected_conditions`를 사용한 명시적 대기

---

### `pytest.ini`
pytest marker를 정리한 설정 파일입니다.

예:
- smoke
- regression
- slow
- fast
- db
- ui
- api

---

## 학습 포인트

이 저장소를 통해 다음 내용을 연습했습니다.

- Python 함수와 클래스 구조 이해
- 입력값 검증 및 예외 처리
- pytest 기반 단위 테스트 작성
- parameterize를 활용한 테스트 확장
- fixture와 conftest를 활용한 공통 설정 분리
- CSV 기반 테스트 데이터 관리
- Selenium을 활용한 UI 자동화 기초
- QA 자동화 학습과 연결되는 Python 테스트 코드 작성 방식 이해

---
