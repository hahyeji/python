# 데이터 자료형(data type)
# 숫자형
# 변수 : 데이터를 담는 그릇, 공간, 컨테이너, 변한다
# 리터럴 : 5, '한'
# 문자, _으로 시작
# 공백x (한글x)
# 예약어 x - CamelCase \ Snake_Case
print(3+3)
print(3+5)
print(3+9)
num1 = 5
num2 = 3.5

# 변수의 데이터 타입 확인 - type()
print(num1+num2)
print(type(num1))
print(type('hello wolrd'))

# 연산자 : +, -, *, /
# a라는 변수를 선언(=메모리의 어떤 공간에 변수를 생성, 주소는 확인가능!)
# id() - 메모리의 주소를 확인하는 함수

#PEP8(python coding convention) 검색해보시오.

a = 20
b = 3
c, d = 20, 30
print("c의 값", c)
print("d의 값", d)
print("두 수의 합은 ", a+b)
print("두 수의 차는 ", a-b)
print("두 수의 곱은 ", a*b)
# int() - 실수 데이터를 저수로 변환하는 함수
print("두 수의 나누기는 ", int(a/b))
print("두 수의 나누기는 ", a//b)
print("두 수의 제곱은 ", a**b)
# 파이썬 연산자 : **, //
# 만능문자, 애스터리스크