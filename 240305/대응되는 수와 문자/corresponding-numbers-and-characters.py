n, m = map(int, input().split())
dic = {}

# 저장
for i in range(n):
    s = input()
    dic[str(i+1)] = s
    dic[s] = i+1

# 조사
for i in range(m):
    s = input()
    print(dic[s])