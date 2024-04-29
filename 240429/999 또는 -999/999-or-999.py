arr = list(map(int, input().split()))
min_val = 999
max_val = -999

for x in arr:
    if x == 999 or x == -999:
        break
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
    
print(max_val, min_val)