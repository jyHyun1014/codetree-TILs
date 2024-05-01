n = int(input())
arr = list(map(int, input().split()))
arr = list(zip(arr, range(n)))
arr.sort()
ans = 0

for x, i in arr:
    for y, j in arr:
        if i < j and ans < y - x:
                ans = y - x
                
print(ans)