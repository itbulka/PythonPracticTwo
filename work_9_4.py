m = [input() for i in range(int(input()))]
n = int(input())
d, lst, s = {}, set(), []
for i in range(n):
    key = input()
    for j in range(int(input())):
        s.append(input())
    d[key] = s
    s =[]
    for k in range(len(d[key])):
        if d[key][k] in m:
            lst.add(key)
s.extend(lst)
print(*s, sep='\n')
