# 리스트 < 튜플 : 속도
# 리스트, 튜플, 딕셔너리, 셋
# list(), tuple(), dict()

# p.72  / 85 /  88 / 97
# 리스트 vs 튜플 : 수정이 가능 vs 수정 불가능
# 튜플의 선언
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1, type(t1))
print(t2)
print(t3)
print(t4, type(t4))
print(t5)

# 튜플의 값을 수정, 삭제할때 (p.86)
# t6 = (1, 2, 'a', 'b')
# del t6[0]
# 튜플 --> 리스트 변경 --> 원소를 조작 --> 튜플
# t7 = list(t6)
# t7[0] = 99
# print(t7)

# 튜플 인덱싱   vs  리스트 인덱싱
# print(t3[5])
# list1 = [1, 3, 5, 7, 9]
# list1[9]
# 튜플 슬라이싱
print(t3[0:2])

# 튜플 + 연산
print(t3+t5)
# * 연산
print(t3 * 3)

print('튜플 t5 길이 : ',len(t5))

empty=[]
for i in range(10):
    empty.append(i)