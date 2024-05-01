n = int(input())
arr = list(map(int, input().split()))
ans = 99

for i in range(n - 1):
    diff = arr[i + 1] - arr[i]
    if diff < ans:
        ans = diff
print(ans)