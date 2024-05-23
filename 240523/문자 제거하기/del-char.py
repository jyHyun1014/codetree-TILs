s = list(input())
end = len(s) - 1

for _ in range(end):
    i = int(input())
    if i >= end:
        del s[end]
    else:
        del s[i]
    end -= 1
    print("".join(s))