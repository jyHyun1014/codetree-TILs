n = int(input())

if n == 2:
    print(28)
else:
    if n % 2 != 0 and n <= 7:
        print(31)
    elif n % 2 == 0 and n <= 7:
        print(30)
    elif n % 2 == 0:
        print(31)
    else:
        print(30)