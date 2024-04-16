start, end = map(int, input().split())
ans = 0
for i in range(start, end + 1):
    cnt = 1
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 3:
        ans += 1
print(ans)