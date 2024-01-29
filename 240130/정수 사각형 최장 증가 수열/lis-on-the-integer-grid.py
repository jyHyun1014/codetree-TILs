n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]    # 1로 초기화 하기

cells = []
ans = 0

# 각 칸에 적혀있는 정수값 기준으로 오름차순 정렬
for i in range(n):
    for j in range(n):
        cells.append((graph[i][j], i, j))
cells.sort()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for v, x, y in cells:
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 해당 인덱스의 값이 존재하고, 현재 값 보다 다음 값이 크다면
        if 0 <= nx < n and 0 <= ny < n and v < graph[nx][ny]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)


# 전체 수들 중에서 최댓값 찾기
for i in range(n):
    ans = max(max(dp[i]), ans)

print(ans)