n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

answer = 0
dic_d = dict()

for elem in d:
    if elem in dic_d:
        dic_d[elem] += 1
    else:
        dic_d[elem] = 1

for i in a:
    for j in b:
        for k in c:
            if -(i + j + k) in dic_d:
                answer += dic_d[-(i + j + k)]
print(answer)