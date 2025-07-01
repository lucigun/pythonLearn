# 파이썬에서 자주 쓰이는 연산자위주로 설명해라

# 산술연산자
# +, -, *, /, //, **, %

# / 의 경우 일반적인 나눗셈, flaot 형태로 나온다.
# // 몪을 구하는 나누셈
# % 나머지를 구하는 나누셈

print(4/2)
print(10//3)
print(10%3)

# ** 제곱을 구한다

print(3**3)

# 정수형끼리 연산 => 정수
# 실수형끼리 연산 => 실수
# 정수형 실수형 연산 => 실수

# 관계연산자
# 대소 비교, 동등비교 시 사용
# >, <, >=, <=, ==, !=
# ==, is 는 서로 다른 연산자 1 == 1 Ture , a is b Ture or False

# 논리연산자
# and , or , not
# and => Ture & True => True
# or => Ture or False => False
# not => Ture or False => Ture

# Boolean
# True, False 판단

print('========================================================')

#산술 연산자 예제를 만들어보라

a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

# 관계연산자를 만들어보라
print(f'{a}는 {b}보다 큽니다. ',a>b )
print(f'{a}는 {b}보다 큽니다. ',a==b)
print(f'{a}는 {b}보다 큽니다. ',a!=b)


