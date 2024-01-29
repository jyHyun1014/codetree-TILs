from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

a = []

for i in range(n):
    for j in range(n):
        a.append((graph[i][j], i, j))

a.sort(reverse=True)

for v, x, y in a:
    temp = []
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and v < graph[nx][ny]:
            temp.append(dp[nx][ny])
    if temp:
        dp[x][y] = max(temp) + 1

ans = 0
for i in range(n):
    ans = max(max(dp[i]), ans)

print(ans)