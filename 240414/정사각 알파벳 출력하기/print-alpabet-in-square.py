n = int(input())

alphabet = ord('A')
for i in range(n):
    for j in range(n):
        print(chr(alphabet), end="")
        alphabet += 1
    print()