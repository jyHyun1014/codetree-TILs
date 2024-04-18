arr = list(map(int, input().split()))
idx = len(arr)
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break

print(*arr[idx-1::-1])