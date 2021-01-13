# p.144 리스트 내포(list comprehensive)
# (java)배열 <---> (python)리스트

a = [1, 2, 3, 4]
print(type(a))
# 리스트 타입, 원소가 x, 빈(empty)
result = []
print(type(a))
print(len(a))

# for i in 반복할 목록(리스트, 튜플, 문자열)
for i in a:
    print(i)

for num in a:
    result.append(num*3)
print('result :', result)

a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

# 랜덤모듈(난수발생) - 파이참, 가상환경(venv)
import random
random_list = []
# .append() : 배열에 값을 추가하는 명령어
# 반복문을 다룰 줄 안다 : while, for
for i in range(10):  # 10 미만까지 뽑아냄
    random_list.append(random.randint(1,10))

print(random_list)