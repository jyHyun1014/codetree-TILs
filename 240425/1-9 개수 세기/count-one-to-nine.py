count_arr = [0] * 9

# 개수 세기
n = int(input())
arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem - 1] += 1

# 개수 출력
for elem in count_arr:
    print(elem)