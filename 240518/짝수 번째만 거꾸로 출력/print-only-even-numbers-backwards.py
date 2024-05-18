s = input()

if len(s) % 2 == 0:
    for i in range(len(s)-1, 0, -2):
        print(s[i], end="")
else:
    for i in range(len(s)-2, -1, -2):
        print(s[i], end="")