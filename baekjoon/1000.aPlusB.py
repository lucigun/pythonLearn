def plus(a,b):
    return a+b

while True:
    try:
        a = int(input('a입력: '))
        break
    except ValueError:
        print('숫자만 입력해야 합니다!')

while True:
    try:
        b = int(input('b입력: '))
        break
    except ValueError:
        print('숫자만 입력해야 합니다!')

print(plus(a, b))