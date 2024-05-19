s = input()
cnt_ee = 0
cnt_eb = 0
for i in range(len(s) - 1):
    if s[i] == 'e':
        if s[i + 1] == 'e':
            cnt_ee += 1
        elif s[i + 1] == 'b':
            cnt_eb += 1
print(cnt_ee, cnt_eb)