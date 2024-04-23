arr = list(map(int, input().split()))

for e in arr:
    if e == 0:
        break
    elif e % 2 == 0:
        print(e // 2, end=" ")
    else:
        print(e + 3, end=" ")