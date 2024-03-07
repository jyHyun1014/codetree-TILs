n , k = map(int, input().split())

arr = list(map(int, input().split()))

count = dict()

# hashmap에 개수 저장
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

# [개수, 숫자] 형태를 리스트로 저장
new_arr = [[value, key] for key, value in count.items()]
new_arr.sort(reverse=True)

for i in range(k):
    print(new_arr[i][1], end=' ')