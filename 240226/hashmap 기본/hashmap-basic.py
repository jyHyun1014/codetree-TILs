n = int(input())
d = dict()
for i in range(n):
    a = input().split()
    if a[0] == 'add':
        d[int(a[1])] = int(a[2])
    elif a[0] == 'remove':
        d.pop(int(a[1]))
    else:
        if int(a[1]) in d:
            print(d[int(a[1])])
        else:
            print('None')