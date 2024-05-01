n = int(input())
price = list(map(int, input().split()))

max_profit = 0
min_price = price[0]
for i in range(n):
    profit = price[i] - min_price

    if profit > max_profit:
        max_profit = profit

    if min_price > price[i]:
        min_price = price[i]
    
print(max_profit)