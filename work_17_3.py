lst = {}
for i in range(int(input())):
    s = input().split()
    value = s[0]+' '+s[1]
    key = s[2]
    if key in lst:
        lst[key].append(value)
    else:
        lst[key] = [value]
for j in range(int(input())):
    k = input()
    print(*lst.get(k, ''))
