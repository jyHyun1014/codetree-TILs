n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i, x in enumerate(arr):
    if x == 2:
        cnt += 1
    if cnt == 3:
        print(i + 1)
        break