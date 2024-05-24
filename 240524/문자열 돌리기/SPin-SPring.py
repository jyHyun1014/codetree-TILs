s = input()
print(s)

for i in range(1, len(s) + 1):
    print(s[-i:]+s[:len(s)-i])