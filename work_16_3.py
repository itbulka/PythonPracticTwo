n = int(input())
lst = []
for i in range(n):
    lst.append([0] * n)
for j in range(n):
    for b in range(n):
        lst[j][b] = int(input())
k = int(input())
for c in range(k):
    y, x = int(input()), int(input())
    lst[x][y] -= 8
    if x - 1 >= 0 and y - 1 >= 0:
        lst[x - 1][y - 1] -= 4
    if x - 1 >= 0:
        lst[x - 1][y] -= 4
    if y - 1 >= 0:
        lst[x][y - 1] -= 4
    if x + 1 < n and y + 1 < n:
        lst[x + 1][y + 1] -= 4
    if x + 1 < n:
        lst[x + 1][y] -= 4
    if y + 1 < n:
        lst[x][y + 1] -= 4
    if x - 1 >= 0 and y + 1 < n:
        lst[x - 1][y + 1] -= 4
    if x + 1 < n and y - 1 >= 0:
        lst[x + 1][y - 1] -= 4
for f in range(n):
    for d in range(n):
        if lst[f][d] < 0:
            lst[f][d] = 0
for i in range(n):
    lst[i] = ' '.join(str(v) for v in lst[i])
print('\n'.join(lst))
