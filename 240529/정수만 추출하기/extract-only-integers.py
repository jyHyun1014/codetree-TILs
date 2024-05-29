a, b= input().split()
c, d = '', ''
for x in a:
    if x.isdigit():
        c += x
    else:
        break
for x in b:
    if x.isdigit():
        d += x
    else:
        break

print(int(c) + int(d))