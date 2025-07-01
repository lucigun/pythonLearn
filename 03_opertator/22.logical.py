# 23.논리,할당,멤버쉽, 부울연산자

# 논리 연산자 예제를 만들어보시오


a = True
b = False

print( a and b)

print ( a or b)

print ( a != b )

print(a, not(a))

if a and b:
    print('TRUE')
else :
    print('FALSE')


if a and b:
    print('TRUE')
else :
    print('FALSE')

print('========================할당=========================')

# 할당 연산자를 만들어보라
# 할당 연산자 : = , +=, -+,


c = 10
print(c)

d = 10
d -= 1
print(d)

d *= 2
print(d)


print('=====================멤버십============================')

# 멤버쉽 연산자 예제
# 멤버십 연산자란? 그룹에 속해있는지 확인하는 연산자, in, is 등

li1= [1,2,3,4,5]
print(li1, type(li1))

a = 10 in li1
print(a)

str = ['a','b','c']

g = 'c' in str
print(g)


print('==================불리언===============================')
# 불리언 연산자

print(bool(0))
print(bool(1))
print(bool(None))

