arr = [
    input()
    for _ in range(10)
]

c = input()
check = True
for word in arr:
    if word[-1] == c:
        print(word)
        check = False

if check:
    print('None')