lst = []
a = int(input())
for i in range(a):
    s = sum((x == y for x, y in zip(lst, reversed(lst))))
    lst.append(s)
print(*lst, sep='\n')
