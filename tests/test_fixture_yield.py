import pytest

@pytest.fixture
def file_writer():
    f = open("test.txt", "w", encoding="utf-8")
    print("파일열기")

    yield f

    print("파일닫기")
    f.close()

def test_write_sentence(file_writer):
    print("테스트시작")
    text = "pytest fixture test\n"

    file_writer.write(text)
    file_writer.flush()

    with open("test.txt", encoding="utf-8") as f:
        content = f.read()

    assert text in content