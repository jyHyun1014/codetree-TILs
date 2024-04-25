count_arr = [0] * 10

# 개수 세기
arr = list(map(int, input().split()))
for elem in arr:
    if elem == 0:
        break
    count_arr[elem // 10] += 1

# 개수 출력
for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")