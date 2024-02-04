n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


# 초기값 세팅
dp[0][0] = graph[0][0]
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], graph[i][0])
for j in range(1, n):
    dp[0][j] = max(dp[0][j - 1], graph[0][j - 1])


for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), graph[i][j])

print(dp[n - 1][n - 1])