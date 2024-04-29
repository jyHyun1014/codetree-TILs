n = int(input())
arr = list(map(int, input().split()))

check = set()
ans = -1

for x in arr:
    if x not in check:
        check.add(x)
        if x > ans:
            ans = x
    
print(ans)