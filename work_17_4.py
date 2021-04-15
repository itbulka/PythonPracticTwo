lst = []
summ, name = 0, ''
for i in range(int(input())):
    k = input().split()
    summ += int(k[-1])
    lst.append(k)
lst[0][-1] = str(summ)
for j in range(len(lst)):
    c = lst[0][0]
    s = lst[j][0]
    for i in range(1, len(lst)):
        if s in lst[i] and c not in lst[i][4]:
            name = lst[i][4]
            cot = int(lst[i][-1])
            for l in range(len(lst)):
                if lst[l][0] in name:
                    lst[l][-1] = str(int(lst[l][-1]) + cot)
for v in lst:
    print(v[-1])

