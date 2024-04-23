n = int(input())
arr = [n * i for i in range(1, 11)]
cnt = 0

for i in arr:
    if i % 5 == 0:
        cnt += 1
    print(i, end=" ")
    if cnt == 2:
        break