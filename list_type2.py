# p.72 리스트 자료형
# 배열(array) - 시퀀스
# 빈 리스트 <--- mutable 변경 가능한 데이터 타입
a = []
b = [1, 2, 3, 'AA','BB',['Life','is', 'egg']]
print('AA' in b)
#list() - 리스트 타입으로 캐스팅(casting) <--> 형변환
# 1. 인덱싱(index) - 값을 가리키는
# index 0 1 2 3 4
str1 = '안녕하세요'
print(str1[0])
print(str1[1])
# print(b[5][0] + b[0])  # formatting 1)% 2).format 3)
print(b[-1])

# 2. 슬라이싱(p.75) : .slice() <---> [시작:끝값:단계]
a = [1,2,3,4,5]
b = [4,5,6]
# >>> : 명령 프롬프트 (CLI)
print(a[0:2])
print(a[2:])

print(a+b)
print(b*3)
print(len(b))

empty_list = []
for i in range(10):
    empty_list.append(i)
print(empty_list)

empty_list = []
for i in range(10):
    empty_list.append(i**2)
print(empty_list)

# 리스트의 수정
empty_list[0]='감'
empty_list[-1]=100
print('-----수정된 리스트의 값-----')
print(empty_list)

# 리스트의 삭제
# 1. del list[인덱스 번호]           <-- (인덱스) 값 제거
# 2. list.remove(리스트 들어있는 값)  <-- (중복된것 중) 첫번째로 나오는 값 제거
# 3. list.pop()                    <-- 마지막 원소를 제거, 기존 리스트를 변환
#    list.pop(x)  x번째(인덱스 번호) 제거
# 4. list.clear()                  <-- 완전히 비워내는

empty_list = []
for i in range(10):
    empty_list.append(i**2)
print(empty_list)

# 리스트 삭제 1번
del empty_list[9]
print('-----변경된 리스트의 값-----')
print(empty_list)

empty_list.append(100)
print(empty_list)

# 리스트 삭제 2번
empty_list.remove(100)
print(empty_list)

# 리스트 삭제 3번
empty_list.pop(7)
print(empty_list)

empty_list.pop()
print(empty_list)

total = 0
for number in empty_list:
    total += number
print('리스트 요소의 합 : ',total)

print('리스트 요소의합 : ',sum(empty_list))  # sum 한줄로 정리

'''
-------리스트 관련 함수-------
1. sum() : 리스트 내의 합(sum)
2. .sort() : 순차정렬해서 출력
3. .reverse() : 역순정렬해서 출력
4. .index(인덱스번호) : 인덱스번호 값 출력
5. .append(추가 될 값) : 리스트의 요소를 리스트 끝에 추가
6. .extend() : 여러개의 요소값을 추가 여러개면([])
7. .insert(인덱스, 값) : (원하는 인덱스 위치에) 요소를 추가
8. .count() : 요소의 갯수
'''
# git으로 파일 버전관리 시작!!

empty_list = []
for i in range(10):
    empty_list.append(i**2)
print(empty_list)

print('합 : ', sum(empty_list))

print(empty_list.reverse())
print(empty_list)
print(empty_list[::-1])  # 이것도 뒤집기
empty_list.append(99)
print(empty_list)
empty_list.insert(0,109)
print(empty_list)
empty_list.extend(['A', 'B', 'C'])
print(empty_list)
empty_list.clear()
print(empty_list)