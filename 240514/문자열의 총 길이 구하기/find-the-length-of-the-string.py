arr = input().split()
answer = 0
for word in arr:
    answer += len(word)
print(answer)