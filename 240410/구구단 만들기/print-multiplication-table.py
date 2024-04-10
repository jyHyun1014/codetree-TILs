a, b = map(int, input().split())

for j in range(1, 10):
    for i in range(b, a - 1, -1):
        if i % 2 == 0:
            print(f"{i} * {j} = {i * j}", end=" ")
            if i > a:
                print("/", end=" ")
    print()