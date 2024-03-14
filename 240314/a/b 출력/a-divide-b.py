a, b = map(int, input().split())

number = a//b
print(number, end="")
print(".", end="")

for i in range(20):
    a = (a - number * b) * 10
    number = a // b
    print(number, end="")