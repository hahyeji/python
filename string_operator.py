# p.49 문자열 연산하기
'''
숫자연산자 : +, -, *, /, %, **, //
문자열연산자 : + (연결)
'''
head = "python"
tail = "is fun"
print(head+tail)

# 문자열 연산자 : * (지정 횟수 반복)
a = 'python'
print('='*50)
print(a*10)
print(10*a)

# len() : 문자열의 길이를 구하는 함수
# p.51
# indexing : 몇번째 문자(열)을 가리키는 것
# python : 갯수 6개
# 012345
print(len(head))
print(head[0], end='')
print(head[1], end='')
print(head[2], end='')
print(head[3], end='')
print(head[4], end='')
print(head[5])

print() 줄바꿈 줄바꿈x---, end='' 줄안바꾸고 이어서 출력하게함

string_a ="Life is too short, you need Python"
string_b ="LIFE IS TOO SHORT, YOU NEED PYTHON"
string_c = string_a[0]+string_a[1]+string_a[2]+string_a[3]
# upper(), lower()
print(string_a.upper())
print(string_b.lower())
print(string_c)
print(string_a[0:4])

# p.53 / slicing : 잘라내는것
# Python만 출력한다면?
# [시작:(끝)]
# [시작:끝(포함x)]
# [시작:끝:단계]
print(string_a[28:])
print(string_a[-1:-7])
print(string_a[19:-7])
print(string_a[1:19:2])

msg_text = 'hello python'
print('python' in msg_text)
print(msg_text[0:11:2])
# Boolean, Bool, 불(부울)


# a = 'text' # 문자열
# b = 10 # 숫자형
# c = True # 논리형 데이터
# d = 4>5 # 비교연산자 True or False로 나옴
print(4 > 5)
print(10 == '10')
print(10 == 10)

