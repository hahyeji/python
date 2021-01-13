# random 모듈을 이용한 (난수 발생) 임의의 숫자값 맞추기 게임
# 1~10 사이의 난수를 발생, 사용자가 입력(input)한 값과 비교(==)
# 난수를 맞추면, 게임종료 + 맞췄습니다. 아니면, 계속 입력하게 하는 것
# 종료 Q 입력시 즉시 종료

# Anaconda3 : 100개 이상의 모듈이 이미 생성
# import random
# while True: # 정답 맞출때까지 계속 반복해서
#     user_input = input('1~10 사이의 숫자를 입력하세요(게임종료 : Q)')
#     if user_input.upper() == 'Q':
#         print('사용자가 게임을 종료했습니다.')
#         break
#     com_input = random.randint(1,10)    # randint(a,b) a부터 b이하까지  randrange(a,b) a부터 b미만까지
#     if int(user_input) == com_input:
#         print('컴퓨터 : ', com_input)
#         print('정답입니다.')
#         break
#     else:
#         print('땡.')

# Quiz. 랜덤값과 사용자 입력값을 비교, 랜덤값을 유추할 수 있도록
# 코드를 수정해보세요!
# ex) 값이 큽니다. 값이 적습니다 등? 맞으면, 게임끝!

# import random
# com_input = random.randint(1,10)
# while True:
#     user_input = input('1~10 사이의 숫자를 입력하세요(게임종료 : Q) ')
#     if user_input.upper() == 'Q':
#         print('사용자가 게임을 종료했습니다')
#         break
#
#     #print('컴퓨터 : ',com_input)
#     if int(user_input) == com_input:
#         print('딩동댕! 맞췄습니다')
#         break
#     elif int(user_input) < com_input:
#         print('값이 큽니다')
#     else:
#         print('값이 작습니다')


import random, time
start_time = time.perf_counter()
com_input = random.randint(1,10)
while True:
    user_input = input('1~10 사이의 숫자를 입력하세요(게임종료 : Q) ')
    if user_input.upper() == 'Q':
        print('사용자가 게임을 종료했습니다')
        end_time = time.perf_counter()
        break
    if int(user_input) == com_input:
        print('딩동댕! 맞췄습니다')
        end_time = time.perf_counter()
        break
    elif int(user_input) < com_input:
        print('값이 큽니다')
    else:
        print('값이 작습니다')
print('-'*30)
print(f'{end_time - start_time}초 걸렸습니다.')
print('-'*30)