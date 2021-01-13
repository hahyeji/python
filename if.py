# p.117 if문
'''
타 프로그래밍 언어     vs    파이썬
----------------------------------
if(조건식) {       if 조건식:
...실행코드...         ...실행코드...
}
if(조건식) {       if 조건식:
...
} else {
....
}
'''

# money = True
# if money:
#     print('택시를 타고 간다')
#     print('택시를 타고 간다')
#     print('택시를 타고 간다')
#     print('택시를 타고 간다')
# else:
#     print('걸어간다.')
#     print('걸어간다.')
#     print('걸어간다.')
#     print('걸어간다.')

# >, <, >=, <=, ==, !=
# if 5>4>3:
#     print('4는 3보다 크고 5보다 작다')
# else:
#     print('4는 3보다 크지 ..않다')

# '''
# 사용자에게 숫자를 하나 입력받고, 이 숫자가 홀수/짝수 여부를 판단하고 내용을 출력하는
# 조건문을 작성해봅시다.
# '''
# # input_num = input('숫자를 하나 입력하세요') ---> 문자열
# # int() : 숫자형으로 변환 (casting, 캐스팅 - 형변환)
# # 홀수 : 1,3,5,7,...  2로 나눈 나머지 값이 - 1
# # 짝수 : 2,4,6,8,10,...                  - 0
# input_num = input('숫자를 하나 입력해보세요')
# input_num = int(input_num)
# if input_num % 2 == 0:
#     print(f'입력한 숫자 {input_num}은 짝수입니다')
# else:
#     print(f'입력한 숫자 {input_num}은 홀수입니다')

input_num2 = input('숫자 입력하세요')
last_char = input_num2[-1]
print(last_char)
if last_char in'02468':
    print('짝')
else:
    print('홀')
# print(input_num2, type(input_num2))






