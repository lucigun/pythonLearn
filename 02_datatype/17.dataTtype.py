# 자료형이란 무엇인지 설명
# 자료형이 무엇인지 확인 시 사용하는 함수
# 자료형을 보여주는 함수를 사용하여 자료형 출력 예제를 만들어보라

# 자료형이란 변수에 저장되어 있는 형태로
# 원시타입과 ?? 타입이 있다
# 원시 타입의 자료형으로는 단순형태, 문자열, 숫자형, 소수형 등 이 있고
# ?? 타입의 경우 복합적인 형태,  list, tuple, dict 등이 있다

a =  100
print(f'a 변수값의 자료형, {a} {type(a)}')
b = 3.14
print(f'b 변수값의 자료형, {b} {type(b)}')
c = 'korea'
print(f'c 변수값의 자료형, {c} {type(c)}')
d = '010-3333-3333'
print(f'd 변수값의 자료형, {d} {type(d)}')
e = 1,2,3,4
print(f'list 변수값의 자료형, {e} {type(e)}')
f = (1,2,3,4,5)
print(f'tpl 변수값의 자료형, {f} {type(f)}')
g = 1,200
print(f'set 변수값의 자료형, {g} {type(g)}')
h = ['korea',1]
print(f'dict 변수값의 자료형, {h} {type(h)}')

print('==================')
# list형 [ ]을 사용한다. 중복이 허용됨
lst = [1,2,3,4]
lst1 = [1,2,1,2]
print('list형',lst)
print('list형',lst1)
# tuple형 ( )을 사용한다.
tup = (1,2,3,4)
print('tuple형',tup)
# set형 { }을사용한다, 중복이 허용되지 않음, 자동으로 소거됨
st = {1,2,3,4,1,2}
print('set형',st)

# dict형  { }를 사용한다. : 를 사요하고 key : value로 처리된다.
dict = {'a':97, 'b':100}
dict1 = {97:'a', 100:'b'}
print('dict형',dict)
print('dict형1',dict1)