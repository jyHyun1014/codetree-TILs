n = int(input())

for i in range(1, n + 1):
    quotient = i // 10  # 몫
    remainder = i % 10  # 나머지
    if i % 3 == 0 or quotient in [3, 6, 9] or remainder in [3, 6, 9]:
        print(0, end=' ')
    else:
        print(i, end=' ')