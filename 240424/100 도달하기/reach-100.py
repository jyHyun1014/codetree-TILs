n = int(input())
arr = [1, n]

for i in range(100):
    sum_val = arr[i] + arr[i + 1]
    arr.append(sum_val)
    print(arr[i], end=" ")
    if arr[i] > 100:
        break