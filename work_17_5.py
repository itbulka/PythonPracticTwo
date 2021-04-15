lst = {}
for i in range(int(input())):
    s = input()
    lst[s] = lst.get(s)
for j in range(int(input())):
    new = ''
    k = False
    for i in input().split('/'):
        if i:
            new = new + '/' + i
        if new in lst:
            k = True
    if k:
        print('YES')
    else:
        print('NO')
