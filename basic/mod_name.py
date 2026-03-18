# mod_name.py
def info():
    print("현재 __name__ : ", __name__)   # 현재모듈(파일)이 어떤방식으로 실행되고있는지

# info()

if __name__ == "__main__":
    print("직접 테스트 중...")
    info()