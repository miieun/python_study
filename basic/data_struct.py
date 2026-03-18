# 리스트
# 리스트 생성
data1 = []
data2 = [1,2,3,4,5]
data3 = ['henry', 'max', 'tom']
data4 = ['henry', 24, 178.5, True]

# 요소추가 
# 리스트.append(추가할요소)
# 리스트.insert(위치,추가할요소)

data3.append("ben")
data3.insert(1,"jin")
print(data3)

# 리스트 수정
data3[0] = "HENRY"
print(data3)

# 삭제
# 리스트.remove(삭제할요소)
# 리스트.pop(인덱스)
# 리스트.clear()
data3.remove("HENRY")
data3.pop(0)
data3.clear()

print(data3)

# 튜플 tuple
# 생성
t1 = ()
t2 = (1,2,3)
t3 = 1,2,3
t4 = (1,)
t5 = ('henry',25, False)

# t5[0] = 'HENRY' #Type error, tuple object does not support item assignment

print(t5[0])

fruit = ("apple", "banna", "orange")
a,b,c = fruit
print(a,b,c)
a, *b = fruit
print(a,b)

# 딕셔너리(dictionary)
# {키 : 값}
# {이름 : [철수,영희,....], 점수 : [90,80,...]}
# {이름:"철수", 나이:39, 결혼유무:False}
# 생성
d1 = {}
d2 = {'이름':"철수", '나이':39, '결혼유무':False , '몸무게':56.7}

# 값추출
print(d2['이름'])

# 추가/수정
# 딕셔너리['추가할키'] = '추가할 값'
d2['이름'] = '영희'
d2['취미'] = '노래'
print(d2)

# 삭제
d2.pop('이름')
print(d2)

d2.clear()
print(d2)

#
d2 = {'이름':"철수", '나이':39, '결혼유무':False , '몸무게':56.7}
print(d2.items())
print(d2.keys())
print(d2.values())



