n = int(input())
lst, ls = {}, []
for i in range(n):
    s, o = input(), int(input())
    lst[o] = s
ls = sorted(lst, reverse=True)
for j in ls:
    for x in lst:
        if x == j:
            print(lst[j])
        else:
            continue
