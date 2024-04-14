n = int(input())

alphabet = ord('A')
for i in range(n):
    for j in range(i + 1):
        print(chr(alphabet), end="")
        if alphabet == 90:
            alphabet = ord('A')
        else:
            alphabet += 1

    print()