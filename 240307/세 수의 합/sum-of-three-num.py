import math

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = dict()
answer = 0

# hashmap에 저장
for elem in arr:
    if elem not in count:
        count[elem] = 1
    else:
        count[elem] += 1

# 배열 순회
for i in range(n):
    # 현재 값은 hashmap에서 빼기
    count[arr[i]] -= 1

    for j in range(i):
        diff = k - arr[i] - arr[j]
        # i 인덱스 이후 arr 배열에 diff가 있으면 그 개수를 답에 더함
        if diff in count:
            answer += count[diff]

print(answer)