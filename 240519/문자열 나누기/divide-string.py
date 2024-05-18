n = int(input())
s = "".join(input().split())

for i in range(0, len(s), 5):
    print(s[i:i + 5])