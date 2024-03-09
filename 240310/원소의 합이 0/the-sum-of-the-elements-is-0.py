n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

answer = 0
dic = dict()

# A 수열에서 숫자 하나, B 수열에서 숫자 하나를 골랐을 때
# 나올 수 있는 두 숫자의 합들을 hashmap에 저장
for i in a:
    for j in b:
        sum_val = i + j
        if sum_val in dic:
            dic[sum_val] += 1
        else:
            dic[sum_val] = 1

for i in c:
    for j in d:
        diff = -(i + j)
        if diff in dic:
            answer += dic[diff]
        
print(answer)