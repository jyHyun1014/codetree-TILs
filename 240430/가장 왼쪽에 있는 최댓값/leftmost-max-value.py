n = int(input())
arr = list(map(int, input().split()))
answer = [1,]
max_val = arr[0]

for i, x in enumerate(arr, start=1):
    if x > max_val:
        answer.append(i)
        max_val = x

for i in range(len(answer) - 1, -1, -1):
    print(answer[i], end=" ")