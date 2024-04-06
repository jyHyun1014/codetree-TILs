n = int(input())

for i in range(n): 
    for j in range(n):
        print(2 * (i + j + 5) + 1, end=" ")
    print()