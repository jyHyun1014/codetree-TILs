cnt_arr = [0] * 4   # A, B, C, D

for i in range(3):
    cold, temp = input().split()
    if cold == 'Y':
        if int(temp) >= 37:
            cnt_arr[0] += 1
        else:
             cnt_arr[2] += 1
    else:
        if int(temp) >= 37:
            cnt_arr[1] += 1
        else:
             cnt_arr[3] += 1

print(*cnt_arr, end=" ")
if cnt_arr[0] >= 2:
    print('E')