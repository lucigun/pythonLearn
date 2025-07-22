#38. 리스트,반복문,요소 값, 거꾸로

# 리스트 요소의 값을 반목문을 사용하여 거꾸로 출력 하시오
lst = ['dog','hippo','elephant','lion','tiger','alligator']


### 거꾸로 출력 [::-1]
print('list역방향 출력')
for i in lst[::-1]:
    print(i, end='\t\t')
print()
print('*'*120)
### 정방출력
print('list정방향 출력')
for i in lst[::1]:
    print(i, end='\t\t')
print()
print('*'*120)

# 인덱스 1부터 정방향 출력
print('lst 인덱스 1부터 정방향 출력')
for i in lst[1::1]:
    print(i, end='\t\t')
print()
print('*'*120)
# 인덱스 0부터 2step씩 정방향 출력
print('lst 인덱스 0부터 2step씩 정방향 출력')
for i in lst[::2]:
    print(i, end='\t\t')
print()
print('*' * 120)
print('lst 인덱스 뒤부터 2step씩 역방향 출력')
# 인덱스 뒤에서 부터 2step씩 역방향출력
for i in lst[::-2]:
    print(i, end='\t\t')



