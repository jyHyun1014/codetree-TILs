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
# 탐색하는 위치의 위에 값과 좌측 값 중에 큰 값과
# 해당 위치의 숫자 중에 최솟값을 구해줍니다.
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), graph[i][j])

print(dp[n-1][n-1])