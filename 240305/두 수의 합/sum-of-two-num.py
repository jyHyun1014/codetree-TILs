n, k = map(int, input().split())
num = list(map(int, input().split()))

count = dict()
answer = 0

for elem in num:
    diff = k - elem
    # count에 diff가 이미 들어있다면 elem과 쌍으로 만들 수 있는 개수가 된다.
    # 즉, 가능한 모든 쌍의 수를 세어준다.
    if diff in count:
        answer += count[diff]
    
    # count 딕셔너리 개수 증가
    if elem not in count:
        count[elem] = 1
    else:
        count[elem] += 1


print(answer)