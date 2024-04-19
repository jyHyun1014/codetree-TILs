n = int(input())
cnt = 0
for i in range(n):
    s = list(map(int, input().split()))
    if sum(s)/4 >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')

print(cnt)