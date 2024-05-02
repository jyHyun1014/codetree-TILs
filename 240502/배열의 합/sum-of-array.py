arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

for row in arr_2d:
    print(sum(row))