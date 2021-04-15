n, m = int(input()), int(input())
lst, lst2 = [], []
s2, s3 = '', ''
for i in range(1, n+1):
    s = input().ljust(m, ' ')
    if i % 2 != 0:
        lst.append(s)
for j in range(len(lst)):
    s2 = lst[j]
    for x in range(len(s2)):
        if x % 2 == 0:
            s3 += s2[x]
    lst2.append(s3)
    s3 = ''
print(*lst2, sep='\n')
