import sys

INT_MAX = sys.maxsize
MAX_BOUND = 100


# 변수 선언 및 입력 받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]    # 해당 위치로 오기 위한 최댓값을 최소로 만드는 경로의 최댓값 저장
answer = INT_MAX


# 초기값 세팅하기
def initialize():
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    dp[0][0] = graph[0][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], graph[i][0])
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], graph[0][j])

# lower_bound 이상의 수들만 사용해서 이동
for lower_bound in range(1, MAX_BOUND + 1):

    # lower_bound 보다 작은 값은 사용 할 수 없도록 변경
    for i in range(n):
        for j in range(n):
            if graph[i][j] < lower_bound:
                graph[i][j] = INT_MAX

    initialize()
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), graph[i][j])

    upper_bound = dp[n-1][n-1]

    if upper_bound != INT_MAX:
        answer = min(answer, upper_bound - lower_bound)
        

print(answer)