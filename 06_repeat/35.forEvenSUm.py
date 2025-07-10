# 짝수 1~100 반복문
# 1부터 100까지 짝수만 출력하는 코드
# 2가지 방식으로 생각해서 출력



# if 조건문을 이용 -> 홀짝 판단 후 처리
for i in range(1,101):
    if i % 2 == 0:
        print(i, end=" ")

print()

# range함수 옵션을 활용할 수 있음
for i in range(2,101,2):
    print(i, end=" ")