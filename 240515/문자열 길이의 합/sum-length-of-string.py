n = int(input())
count = 0
a_count = 0
for _ in range(n):
    word = input()
    count += len(word)
    if word[0] == 'a':
        a_count += 1
print(count, a_count)