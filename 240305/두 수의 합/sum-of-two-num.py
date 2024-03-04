import math

n, k = map(int, input().split())
data = {}
pair = set()
answer = 0
num = list(map(int, input().split()))

for i in range(n):
    if num[i] not in data:
        data[num[i]] = 1
    else:
        data[num[i]] += 1

if k % 2 == 0:
    if k//2 in data and data[k//2] >= 2:
        answer += math.comb(data[k//2], 2)

num = list(data.keys())
num.sort()

for i in range(len(num)):
    if num[i] >= k / 2:
        break
    if k - num[i] in data:
        answer += (data[num[i]] * data[k - num[i]])

print(answer)