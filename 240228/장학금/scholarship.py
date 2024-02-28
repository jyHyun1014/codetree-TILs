mid, final = map(int, input().split())

if mid < 90 or final < 90:
    print(0)
elif final >= 95:
    print(100000)
else:
    print(50000)