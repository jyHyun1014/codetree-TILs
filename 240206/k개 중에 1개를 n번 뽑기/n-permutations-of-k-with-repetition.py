n, k = map(int, input().split())
answer = []
def choose(length):
    if length == n:
        print(*answer)
        return

    for i in range(1, k+1):
        answer.append(i)
        choose(length + 1)
        answer.pop()
    return

choose(0)