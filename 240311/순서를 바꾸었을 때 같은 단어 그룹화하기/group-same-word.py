from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    word = list(input())    # 단어 문자열을 리스트로 변환
    word.sort()             # 단어 정렬
    word = "".join(word)    # 리스틑를 문자열로 변환
    dic[word] += 1          # 단어를 key로, 개수를 value로 저장

# dic의 value 중에 max 값 출력
print(max(list(dic.values())))