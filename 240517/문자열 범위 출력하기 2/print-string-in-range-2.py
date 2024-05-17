s = input()
n = int(input())

if len(s) >= n: 
    for i in range(-1, -n - 1, -1):
        print(s[i], end="")
else:
    for i in range(-1, -len(s) - 1, -1):
        print(s[i], end="")