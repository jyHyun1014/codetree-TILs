n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[1000000] * n for _ in range(n)]


# 초기 세팅
dp[0][n-1] = graph[0][n-1]

for j in range(n-2, -1, -1):
    dp[0][j] = dp[0][j+1] + graph[0][j]

for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + graph[i][n-1]


# DP
for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1] + graph[i][j], dp[i-1][j] + graph[i][j])

print(dp[n-1][0])

# 풀이
# 2  2  2 1
# 5  4  3 2
# 8  7  6 2 
# 11 10 9 2
# 순서로 업데이트 하기