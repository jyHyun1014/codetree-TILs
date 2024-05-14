arr = ["apple", "banana", "grape", "blueberry", "orange"]
c = input()
count = 0
for word in arr:
    if word[2] == c or word[3] == c:
        print(word)
        count += 1
print(count)