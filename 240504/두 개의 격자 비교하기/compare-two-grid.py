n, m = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()