a = input()
b = input()
n = len(b)

while True:
    i = a.find(b)
    if i == -1:
        break
    a = a[:i] + a[i+n:]
print(a)