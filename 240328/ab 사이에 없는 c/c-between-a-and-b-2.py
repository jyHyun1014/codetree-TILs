a, b, c = map(int, input().split())
check = True
for i in range(a, b + 1):
    if i % c == 0:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')