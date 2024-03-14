a, b = map(int, input().split())

# 정수 부분 먼저 출력
print(f"{a//b}.", end="")

for _ in range(20):
    a %= b  # a를 b로 나눈 나머지
    a *= 10 # 나머지에 10 곱하기
    print(a // b, end="")