# 기본적인 if else 조건문 if elif else 조건문 예제를 구현하시오

a = 101


if a > 100:
    print(f'a는 100보다 큽니다. {a}입니다.')
elif a > 50:
    print(f'a는 50보다 큽니다. {a}입니다.')
else:
    print(f'a는 {a}입니다.')


b = 30
if b == 20 :
    print(f'b는 20입니다.')
else:
    print(f'b는 20이 아닙니다. {b}입니다.')


c = '바나나스'
d = ['바나나','바나나스']

if c in d :
    print(f'd 그룹에는 {c}가 포함되어 있습니다. C는 {c}이고 d는 {d}입니다.')
else:
    print(f'd 그룹에는 {c}가 포함되어있지 않습니다.C는 {c}이고 d는 {d}입니다.')