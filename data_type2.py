'''
    변수의 자료형
    1. 숫자형 / int , float , complex
    2. 문자(열)형 / string
    3. 논리형 / boolean
'''
text1 = "hello"
text2 = 'world'
# + : 덧셈연산자, (문자) 연결 연산자
print(text1+' '+text2)
# html, css - "" / javascript, python, php - ''

# 문자(열)형 데이터
pet_name = "율무"
pet_age = 5
pet_type = "cat"
pet_weight = 4
print(pet_name+"는 "+str(pet_age)+"살 이고, 몸무게는 "+str(pet_weight)+"kg 입니다")
print(pet_name,"는 ",pet_age,"살 이고, 몸무게는 ",pet_weight,"kg 입니다")
# python 3.6 이상 도입된 f-string 방식
print(f"{pet_name}라는 {pet_type}를 키운지 몇년이 되었는데, 벌써 {pet_age}살이고 몸무게는 {pet_weight}kg이 되었다.")

python_string = 'life is short, you need python'
# len() 함수
print('문자열 길이값', len(python_string))
# 문자열 인덱스/index - 문자열 데이터의 하나하나 값을 주소/번지로 구분하는 것
# 변수 - 변하는 데이터, 변할 수 있는
# 문자(열) - 변경 금지!
print(python_string[0])
print(python_string[6])
print(python_string[-1])
print(python_string[-5])
print(python_string[-2])
print(python_string)
