# 36. 구구단, 반복문, 중첩, 이중 반목문
# for를 사용한 구구단 전체를 출력


# for i in range (2,10) :
#     for j in range (1, 10):
#         if j <= 10:
#             print(f'{i}X{j}={i * j}')
#             j += 1
#         else:
#             print()


for i in range(2,10):
    print(i,'단')
    for j in range(1,10):
        print(i,'x',j,'=',i*j)
    print()


print("*"*120)

for a in range(2,10):
    for c in range(1,10):
        if c <= 10:
            print(f'{a}X{c}={a*c}', end="\t")
            if c == 9:
                print()
        else:
            print()

