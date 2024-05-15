arr = [
    input()
    for _ in range(10)
]

c = input()

for word in arr:
    if word[-1] == c:
        print(word)