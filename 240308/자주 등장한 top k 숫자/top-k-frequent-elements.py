n , k = map(int, input().split())

arr = list(map(int, input().split()))

count = dict()
count2 = dict()

for elem in arr:
    if elem in count:
        count2[count[elem]].remove(elem)
        count[elem] += 1
        if count[elem] not in count2:
            count2[count[elem]] = set()
        count2[count[elem]].add(elem)

    else:
        count[elem] = 1
        if 1 not in count2:
            count2[1] = set()
        count2[1].add(elem)

count2_list = list(count2.keys())
count2_list.sort(reverse=True)

# print(count2_list)

check=False
temp = 0
for i in count2_list:
    ans = list(count2[i])
    ans.sort(reverse=True)
    for a in ans:
        print(a, end=' ')
        temp += 1
        if temp == k:
            check=True
            break
    if check:
        break