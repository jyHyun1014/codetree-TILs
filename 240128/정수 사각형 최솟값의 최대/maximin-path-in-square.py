n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


# 초기값 입력
dp[0][0] = graph[0][0]

for j in range(1, n):
    dp[0][j] = min(dp[0][j-1], graph[0][j])

for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], graph[i][0])


# DP
for i in range(1, n):
    for j in range(1, n):
        temp = [(dp[i-1][j], 0), (dp[i][j-1], 1), (graph[i][j], 2)]
        temp.sort()
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], graph[i][j])
        if temp[0][1] == 2:
            dp[i][j] = graph[i][j]
        elif temp[0][1] == 0:
            dp[i][j] = min(dp[i][j-1], graph[i][j])
        else:
            dp[i][j] = min(dp[i-1][j], graph[i][j])

print(dp[n-1][n-1])