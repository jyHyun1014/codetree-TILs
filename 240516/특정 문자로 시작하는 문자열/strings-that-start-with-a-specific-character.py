n = int(input())

arr = [
    input()
    for _ in range(n)
]

c = input()
count = 0
total = 0

for word in arr:
    if word[0] == c:
        count += 1
        total += len(word)

print(f"{count} {total/count:.2f}")