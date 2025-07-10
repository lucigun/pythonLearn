#34.홀수, 홀수합, 반복문

# for를 사용해서 4부터 21까지 홀 수 합을 구하라

first = 4
last = 21

sum = 0

for i in range(first,last+1):
    # print(i, end='\t')
    if (i % 2 == 1):
        sum +=i

print(sum)

print ('*'*100)
s = 4
l = 21

sum1 = 0
for i in range(s, l+1):
  if (i % 2) == 1:
    sum1 += i

print(sum1)