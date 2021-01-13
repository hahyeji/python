# if만 이용해서 홀, 짝

input_num = input('숫자 입력하세요')
last_char = input_num[-1]
if last_char in '02468':
    print('짝')

if last_char in '13579':
    print('홀')