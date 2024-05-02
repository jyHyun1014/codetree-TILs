arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    print(f"{sum(arr_2d[i]) / 4:.1f}", end=" ")
print()

for j in range(4):
    print(f"{(arr_2d[0][j] + arr_2d[1][j]) / 2:.1f}", end=" ")
print()

total = 0
for i in range(2):
    for j in range(4):
        total += arr_2d[i][j]
print(f"{total / 8:.1f}")