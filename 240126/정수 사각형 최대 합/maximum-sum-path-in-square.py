n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

total = 0
for i in range(n):
    total += graph[0][i]
    dp[0][i] = total

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i][j-1] + graph[i][j])


print(dp[n-1][n-1])

# 문제 풀이
# 1 2 3 4 
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 순서로 구하면 됨