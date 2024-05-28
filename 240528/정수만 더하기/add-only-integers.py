s = input()
ans = 0
for x in s:
    if x.isdigit():
        ans += int(x)
print(ans)