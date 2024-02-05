n = int(input())

start = input()
target = input()

w = 0
b = 0
for i in range(n):
    if start[i] != target[i]:
        if start[i] == 'W':
            w += 1
        else:
            b += 1

print(max(w, b))