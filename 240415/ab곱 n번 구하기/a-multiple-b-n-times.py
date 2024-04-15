n = int(input())

for _ in range(n):
    result = 1
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        result *= i
    print(result)