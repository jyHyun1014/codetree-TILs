a = input()
b = input()
answer = 0 
for i in range(len(a) - 1):
    if a[i:i+2] == b:
        answer += 1
print(answer)