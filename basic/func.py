# 함수
def rect_area(x,y):
    print(f"사각형의 넓이는 {x,y} 입니다")

def rect_area1(x,y):
    return x*y

def rect_area2(x,y):
    return x*y, (x+y)*2

print(rect_area1(10,20))

area, length = rect_area2(10,20)
print(area, length)

# 정수를 입력하면 짝수인지 홀수인지 판별해주는 함수
def odd_even(x):
    if x % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result

# print(odd_even(2))
# print(odd_even(7)

# num = int(input("숫자를 입력해주세요"))
# odd_even(num)
# print(f"입력 값 {num}은/는 {odd_even(num)}입니다")


# 매개변수의 기본값 미리 지정하는 경우
def like_fruit(name, fruit="apple"):
    print(f"{name}님이 제일 좋아하는 과일은 {fruit}입니다.")

like_fruit("이순신")
like_fruit("이순신","orange")
like_fruit(fruit="orange",name="이순신")

# 정해지지 않은 개수의 매개변수로 함수 정의하는 경우
def avg(*num):
    sum = 0
    cnt = len(num)
    for i in num:
        sum = sum + i
    return sum / cnt

print(avg(10,20,30))
print(avg(10,20,30,50,60))
print(avg(10,20))

# 지역변수, 전역변수
pi = 3.14
def circle_area(r):
    global pi   # pi = 3.1
    area = r * r * pi
    return area

result = circle_area(10)
print(f"원의 넓이는 {result}입니다")

#lambda
add = lambda x, y : x+y
print(add(10,5))

is_even = lambda x : "짝수" if x % 2 ==0 else "홀수"
print(is_even(9))

grade = lambda score: "A" if score >=90 else ("B" if score >=80 else "C")
print(grade(95))

# 예외처리
try :
    a =4    #int(input("인원입력:"))
    b =1000 # int(input("금액입력:"))
    c = b / a
except ValueError:
    print("숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print((f"에러 : {e}"))
else:
    print(f"한사람당 {c}원씩 나누면 됩니다")
finally:
    print("완료")

# 파일오픈
try:
    f = open("output.txt", "r")
except Exception as e:
    print(f"에러 : {e}")
else:
    print("파일열기 성공")
    f.close()

# raise
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다!")  # 직접 예외 발생
    return a / b
print(divide(5, 0))   # ZeroDivisionError 발생

def set_age(age):
    if age < 0 :
        raise ValueError("나이는 0 이상이어야 합니다")
    return f"당신의 나이는 {age}살입니다."

print(set_age(-3))