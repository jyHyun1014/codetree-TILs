from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    word = list(input())
    word.sort()
    word = "".join(word)
    dic[word] += 1

print(max(list(dic.values())))