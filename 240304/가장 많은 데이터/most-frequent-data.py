n = int(input())
freq = {}   # 문자열의 등장 횟수

# 문자열의 등장 횟수 저장
for i in range(n):
    s = input()
    if s not in freq:
        freq[s] = 1
    else:
        freq[s] += 1

# 값들의 최댓값 출력
print(max(list(freq.values())))