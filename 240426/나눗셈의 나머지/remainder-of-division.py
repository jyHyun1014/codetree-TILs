a, b = map(int, input().split())
cnt_arr = [0] * b
ans = 0

while a > 1:
    cnt_arr[a % b] += 1
    a //= b

for x in cnt_arr:
    ans += (x ** 2)
print(ans)