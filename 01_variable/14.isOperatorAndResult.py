# 14. is연산자, 결과, print

is연산자 결과 및 print 결과를

a = 'korea'
print('[1]',a,id(a))

# korea, a 메모리주소

b = 'korea'
print('[2]',b,id(b))
# korea, a메모리주소
print('a is b = ', a is b)
# a is b = True

b += "!"
print('[3]', b, id(b))
# korea!, b메모리주소
print('a is b =', a is b)
# a is b = False

c = b[:-1]
print('[4]', c, id(c))
# korea, a메모리주소
# 정답은 korea, c메모리주소
print('a is c =', a is c)
# a is c = True
# a is c = Fasle