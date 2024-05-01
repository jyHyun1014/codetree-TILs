arr = list(map(int, input().split()))
max_val = 1
min_val = 1000

for x in arr:
    if x < 500 and x > max_val:
        max_val = x
    elif x > 500 and x < min_val:
        min_val = x
print(max_val, min_val)