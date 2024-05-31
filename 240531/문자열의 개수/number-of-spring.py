arr = []
while True:
    s = input()
    if s == '0':
        break
    arr.append(s)

print(len(arr))

for i in range(0, len(arr), 2):
    print(arr[i])