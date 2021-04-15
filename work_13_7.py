n = int(input())
lst = [input() for i in range(n)]
a = int(input())
d = []
while True:
    if len(lst) > 0:
        d.append(lst[0])
        lst.pop(0)
        n -= 1
    else:
        break
    t = 1
    for i in range(n // a):
        d.append(lst[((i + 1) * a) - t])
        lst.pop(((i + 1) * a) - t)
        n -= 1
        t += 1
print(*d, sep='\n')
