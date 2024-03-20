sum_val = 0
count = 0

for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum_val += n
        count += 1

print(f"{sum_val} {sum_val / count:.1f}")