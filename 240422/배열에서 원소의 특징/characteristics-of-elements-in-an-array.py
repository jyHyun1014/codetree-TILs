arr = list(map(int, input().split()))

for i in range(1, 10):
    if arr[i] % 3 == 0:
        print(arr[i - 1])
        break