# 1~10까지 합 구하기

sum = 0
for i in range(1,11):
    sum = sum + i

print(sum)

for i in "apple":
    print(i)

for i in ['a',1, False]:
    print(i)

i = 1
sum = 0
while i < 11:
    sum = sum + i
    i = i + 1
print(sum)

# break
sum = 0
i = 1
while True:
    sum = sum + i
    i = i + 1
    if i > 10 : 
        break  
print(sum)

# 1~10 홀수만 출력
for i in range(1,11,2):
    print(i)

# i = 1
# while i < 11 :
#     print(i)
#     i = i + 2

i = 0
while i < 10 :
    i = i + 1
    if i % 2 == 0 :
        continue
    print(i)

# 노래 가사 출력
for i in range(1, 11, 1):
    print(f"{i} 마리 코끼리가 거미줄에 걸렸네")

# 10부터 0까지 거꾸로 카운트다운
for i in range(10, -1, -1):
    print(i)

i = 10
while i > -1 :
    print(i)
    i = i -1  # i -= 1 

# 구구단 출력
dan = int(input("숫자를 입력하세요:"))
for i in range(1,10):
    print(f"{dan} x {i} = {dan*i}")

# 한 줄에 하나씩 이름 출력
data = 'Jhop, RM, jimin, jonguk'
print(data.split(','))
for i in data.split(',') :
    print(i.strip())    # strip()은 공백 빼고


# 1부터 30까지의 숫자 중에서 3의 배수만 출력하세요
for i in range(1, 31):
    if i % 3 == 0:
        print(i)


# 사용자로부터 4자리 숫자로 구성된 비밀번호를 입력받기
while True:
    pw = input("4자리 비밀번호를 입력하세요: ")

    if pw == '0418' :
        print("비밀번호가 맞습니다")
        break
    else:
        print("비밀번호가 틀렸습니다")


# 확장자 제거 후 파일이름만 출력
filelist = ['f1.csv', 'f2.csv', 'f3.csv', 'f4.csv', 'f5.csv']

for i in filelist:
    print(i.split(".")[0])
