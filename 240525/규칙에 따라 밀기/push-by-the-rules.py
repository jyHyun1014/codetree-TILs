a = input()
q = input()
for x in q:
    if x == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]
print(a)