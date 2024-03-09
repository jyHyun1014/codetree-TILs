n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = set(map(int, input().split()))
answer = 0

for i in a:
    for j in b:
        for k in c:
            if -(i + j + k) in d:
                answer += 1
print(answer)