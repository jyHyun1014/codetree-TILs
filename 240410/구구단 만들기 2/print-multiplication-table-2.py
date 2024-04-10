a, b = map(int, input().split())

for j in [2, 4, 6, 8]:
    for i in range(b, a - 1, -1):
        print(f"{i} * {j} = {i * j}", end=" ")
        if i > a:
            print("/", end=" ")
    print()