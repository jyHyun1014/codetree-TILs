n = int(input())
x = 1
while True:
    if 2 ** x == n:
        print(x)
        break
    else:
        x += 1