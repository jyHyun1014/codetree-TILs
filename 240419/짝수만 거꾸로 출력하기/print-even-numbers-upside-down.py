n = int(input())
arr = list(map(int, input().split()))
ans_arr = []
for elem in arr:    
    if elem % 2 == 0:
        ans_arr.append(elem)
print(*ans_arr[::-1])