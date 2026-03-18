# 조건문
score = 50
if score >= 80 :
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")

# 주민번호를 가지고 있는 id에서 성별을 분석하여
# '남성', '여성'으로 출력하세요
id = "260313-3******"
if id[7] == "1" or id[7] == "3":
    print("남성")
elif id[7] == "2" or id[7] == "4":
    print("여성")
else: 
    print("잘못된 id입니다")

# if id[7] in ["1","3"]:
#     print("남성")
# elif id[7] in ["2","4"]:
#     print("여성")

# 날짜가 짝수면 "짝수번호 차량 통행가능"
# 날짜가 홀수면 "홀수번호 차량 통행가능"
date = "2026-03-13"
# print(date.split('-'))
num = int(date.split('-')[2])
if num % 2 == 0:
    print("짝수 차량 통행가능")
else:
    print("홀수 차량 통행가능")

# if int(date[-1]) % 2 == 0:
#     print("짝수번호 차량 통행가능")
# elif int(date[-1]) % 2 == 1:
#     print("홀수번호 차량 통행가능")

# 구매금액 + 배송비(3000원), 5만원 이상은 무료배송
# 총 결제금액을 출력 
# 조건 if만 사용
# price = 55000

# total = price

# if price < 50000:
#     total = price + 3000

# print("총 결제금액:", total)

price = 30000
if price < 50000:
    price = price + 3000

print(f"결제금액:{price}")