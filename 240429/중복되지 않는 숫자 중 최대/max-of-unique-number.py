n = int(input())
arr = list(map(int, input().split()))
ans = -1

for x in set(arr):
    if arr.count(x) == 1 and x > ans:
        ans = x
    
print(ans)