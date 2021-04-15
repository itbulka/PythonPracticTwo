s = int(input())
lst, lst2, count = [], [], 0
for i in range(s):
    s1 = int(input())
    lst.append(s1)
    lst2.append(s1)
n = int(input())
for j in range(n):
    b, p, k = int(input()), int(input()), int(input())
    if b == 1:
        lst[p] = lst[p] + k
    else:
        lst2[p] = lst2[p] + k
for h in range(len(lst)):
    if lst[h] == lst2[h]:
        count += 1
print(*lst)
print(*lst2)
print(count)
