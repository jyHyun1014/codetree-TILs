n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = graph[0][0]

for j in range(1, n):
    dp[0][j] = dp[0][j-1] + graph[0][j]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i][j-1] + graph[i][j])

print(dp[n-1][n-1])

# 문제 풀이
# 1 1 1 1 
# 1 2 3 4
# 1 5 6 7
# 1 8 9 10
# 순서로 구하면 됨