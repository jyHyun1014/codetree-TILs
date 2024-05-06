n, m = map(int, input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for j in range(m):
    k = 0
    while j - k >= 0 and k < n:
        arr[k][j - k] = num
        k += 1
        num += 1
    
for i in range(1, n):
    k = 0
    while i + k < n and m - 1 - k >= 0:
        arr[i + k][m - 1 - k] = num
        k += 1
        num += 1

# 출력
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()