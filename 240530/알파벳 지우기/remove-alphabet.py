a = input()
b = input()
c, d = '', ''

for x in a:
    if x.isdigit():
        c += x
for x in b:
    if x.isdigit():
        d += x

print(int(c) + int(d))