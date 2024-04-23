arr = list(map(int, input().split()))

for i in range(8):
    arr.append(arr[i + 1] + 2 * arr[i])

print(*arr)