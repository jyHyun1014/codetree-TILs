n = int(input())

check = False
for i in range(2, n):
    if n % i == 0:
        check = True
        break

if check:
    print("C")
else:
    print("N")