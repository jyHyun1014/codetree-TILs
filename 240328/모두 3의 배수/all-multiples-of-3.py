check = True
for _ in range(5):
    n = int(input())
    if n % 3 != 0:
        check = False
        break

print(int(check))