# 파이썬 기본적인 변수 선언과 변수 할당을 보여주는 코드를 구현하시오
# [결과출력]
# 100
# 3.14
# 100 3.14 k Hello World


a = 100
b = 3.14
c = 'k'
d = 'Hello World'

print('1번 문제')
print(a)
print(b)
print(a,b,c,d)
print(f'{a} {b} {c} {d}')


print('======절취선======')
# 변수값 할당 시 여러변수에 동시에 한개의 값을 할당하는 다중할당 코드를 구현하시오

# e = 100
# f = e
# g = f

e = f = g = 100

print('2번문제')
print(e,f,g,e)