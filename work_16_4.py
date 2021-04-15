n = int(input())
lst = [[]]
for i in range(n - 1):
    lst.append([int(j) for j in input().split()])
station = input().split()
a, a1 = int(station[0]), int(station[1])
lk = lst[max(a, a1)][min(a, a1)]
b = -1
for x in range(n):
    if x != a and x != a1:
        if (lk > lst[max(a, x)][min(a, x)] + lst[max(x, a1)][min(x, a1)]):
            lk = lst[max(x, a1)][min(x, a1)] + lst[max(x, a1)][min(x, a1)]
            b = x
if b != -1:
    print(b)
else:
    print(a)
