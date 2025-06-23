# 16.값 교환, temp, 두변수값 교환

# a, b 각 변수의 값을 교환하는 코드 작성

a = 100
b = 200

print('a,b 변수 값은 =', a, b)

print(f'교환전 a, b 변수의 값은 = {a} {b}')

# 일반적인 temp를 이용한 swap

temp = a
a = b
b = 100

print(f'임시 {temp} 교환 후 a, b 변수의 값은 = {a} {b}')


# c,d 변수 값을 교환하는 코드를 작성
# c,d 100 200
#별도 temp를 만들지 말고 한줄로 코드를 작성하여 교환

c = 100
d = 200
print(f'교환전 c는 {c}, d는 {d}')
c , d = d , c
print(f'교환후 c는 {c}, d는 {d}')