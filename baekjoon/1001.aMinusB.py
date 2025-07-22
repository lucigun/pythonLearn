# 두 정수를 입력받아 a-b를 출력하는 프로그램을 작성하라

def minus(a,b):
    return a-b

while True:
    try:
        a = int(input('a입력'))
        break
    except ValueError:
        print('다시입력하세요')
while True:
    try:
        b = int(input('b입력'))
        break
    except ValueError:
        print('다시입력하세요')

print(minus(a,b))