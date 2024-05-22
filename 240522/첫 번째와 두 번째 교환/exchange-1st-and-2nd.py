s = list(input())

a = s[0]
b = s[1]

for i in range(len(s)):
    if s[i] == a:
        s[i] = b
    elif s[i] == b:
        s[i] = a

print(''.join(s))