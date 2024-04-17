arr = list(map(int, input().split()))
sum_val = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] >= 250:
        break
    else:
        sum_val += arr[i]
        cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")