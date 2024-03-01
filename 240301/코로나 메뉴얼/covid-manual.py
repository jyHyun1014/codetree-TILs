count = 0
for i in range(3):
    cold, temp = input().split()
    if cold == 'Y' and int(temp) >= 37:
        count += 1
if count >= 2:
    print('E')
else:
    print('N')