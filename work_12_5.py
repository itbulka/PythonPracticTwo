n = int(input())
lst, pd, i = [], [], 1
while i not in lst:
    lst.append(i)
    print(lst)
    pd.append(10*i//n)
    print(pd)
    i = 10 * i % n
    print(i)
print(*pd[lst.index(i):], sep='')
