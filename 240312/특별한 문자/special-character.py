from collections import defaultdict

text = input()
dic = defaultdict(int)
answer = ""

# key에 문자를, value에 개수를 저장
for c in text:
    dic[c] += 1

# value가 1인 key 찾기
for c in text:
    if dic[c] == 1:
        answer = c
        break

if answer == "":
    answer = "None"

print(answer)