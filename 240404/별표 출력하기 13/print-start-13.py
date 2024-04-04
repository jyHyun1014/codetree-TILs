n = int(input())
cnt_odd = 1
cnt_even = n
for i in range(2 * n):
    if i % 2 == 0:
        for j in range(cnt_even):
            print("*", end=" ")
        print()
        cnt_even -= 1
    else:
        for j in range(cnt_odd):
            print("*", end=" ")
        print()
        cnt_odd += 1