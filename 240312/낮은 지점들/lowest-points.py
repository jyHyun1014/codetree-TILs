n = int(input())
dic = dict()

for _ in range(n):
    x, y = map(int, input().split())

    if x in dic:
        dic[x] = min(dic[x], y) # 더 작은 y값 저장
    else:
        dic[x] = y

# dic 값들의 합 출력
print(sum(dic.values()))