a = input()
q = input()
cnt = 0
for x in q:
    if x == 'L':
        cnt += 1
    else:
        cnt -= 1

print(a[cnt:] + a[:cnt])