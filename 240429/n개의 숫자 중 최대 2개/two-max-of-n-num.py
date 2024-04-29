n = int(input())
arr = list(map(int, input().split()))

first = max(arr[0], arr[1])
second = min(arr[0], arr[1])

for i in range(2, n):
    if arr[i] > first:
        first, second = arr[i], first
    elif arr[i] > second:
        second = arr[i]
    
print(first, second)