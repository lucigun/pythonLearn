# 13. is,==연산자

is, == 연산자 결과로 출력되는 값을 예상하라

# [1] : 숫자
a = 100
b = 100 + 1

print('[1-1] a is b =', a is b ) #false
print('[1-2]a == b =', a == b ) # false

# [2] 문자열
c = 'korea'
d = 'korea'

print('[2-1] c is d =', c is d ) # false
print('[2-2] c == d =', c == d ) # true

#[3] : 리스트
e = [1,2,3,4,5]
f = [1,2,3,4,5]

print('[3-1] e is f =' , e is f ) # fals
print('[3-2] e == f =', e == f ) #ture

print(id(c))
print(id(d))

