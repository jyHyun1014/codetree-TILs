a = input()
b = input()
ans = 0
check = False

for i in range(len(a)):
    if a == b:
        print(ans)
        check = True
        break
    a = a[len(a) - 1] + a[:len(a) - 1]
    ans += 1

if not check:
    print(-1)