n = int(input())
arr = [1, n]

for i in range(100):
    sum_val = arr[i] + arr[i + 1]
    print(sum_val, end=" ")
    if sum_val > 100:
        break
    else:
        arr.append(sum_val)