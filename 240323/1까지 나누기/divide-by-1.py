n = int(input())
count = 0
div = n
for i in range(1, n + 1):
    div /= i
    count += 1
    if div <= 1:
        print(count)
        break
    div = int(div)