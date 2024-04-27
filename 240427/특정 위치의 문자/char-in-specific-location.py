word = ['L', 'E', 'B', 'R', 'O', 'S']
c = input()

# 해당 문자가 리스트에 없는 경우
if c not in word:
    print("None")
# 해당 문자가 리스트에 있는 경우
else:
    print(word.index(c))