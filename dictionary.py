# 딕셔너리 자료형 (p.88)
# 리스트 == 배열 [ , ]
# 딕셔너리 = 객체 (키 : 값)
# 홍길동, 1월 13일(생일), 성별(남자), 키, 시력
person = ['홍길동','0113','남',175,1.0,1.5]
#빈 딕셔너리 생성
person1 = {}
person1['id']='abcd1234'
person1['nick']='big apple'
person1['level']=99
person1['hp']=1000
person1['mp']=50
print(person1)

# 딕셔너리, 초기화
person2 = {
    'name':'홍길동',
    'birth':'0113',
    'gender':'남',
    'height':175
}
print(person2)

for property in person1:
    print(property,':',person1[property])