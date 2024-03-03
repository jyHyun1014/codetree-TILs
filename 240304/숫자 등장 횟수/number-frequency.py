n, m = map(int, input().split())
data = list(map(int, input().split()))
ques = list(map(int, input().split()))

dic = {}

# 딕셔너리에 값 넣기
for i in range(n):
    if data[i] in dic:
        dic[data[i]] += 1
    else:
        dic[data[i]] = 1

# 딕셔너리에 값 탐색하기
for i in range(m):
    if ques[i] in dic:
        print(dic[ques[i]], end=' ')
    else:
        print(0, end=' ')