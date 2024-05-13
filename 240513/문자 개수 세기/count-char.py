from collections import Counter

s = input()
alpha = input()
counter = Counter(s)
print(counter[alpha])