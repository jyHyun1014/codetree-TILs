n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
for j in range(-1, -n - 1, -1):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = num
            num += 1
    else:
        for i in range(n - 1, -1, -1):
            arr[i][j] = num
            num += 1


# 출력
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()