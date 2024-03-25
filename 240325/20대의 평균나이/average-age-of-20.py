total = 0
count = 0
while True:
    n = int(input())

    if n < 20 or n >= 30:
        print(f"{total/count:.2f}")
        break 

    total += n
    count += 1