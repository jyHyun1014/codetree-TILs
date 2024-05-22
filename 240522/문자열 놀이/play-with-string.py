s, q = input().split()
s = list(s)

for _ in range(int(q)):
    n, a, b = input().split()

    if n == '1':
        s[int(a) - 1], s[int(b) - 1] = s[int(b) - 1],  s[int(a) - 1]
        print(''.join(s))
    else:
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print(''.join(s))