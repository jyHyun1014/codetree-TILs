s = input()

encoding = [[s[0], 1]]

for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        encoding[-1][1] += 1
    else:
        encoding.append([s[i], 1])

answer = ""
for x, cnt in encoding:
    answer += (x + str(cnt))

print(len(answer))
print(answer)