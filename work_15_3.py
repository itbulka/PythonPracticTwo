s = input()
lst = [s[j] for j in range(len(s))]
m = []
for i in range(len(lst)):
    m.append(s.count(lst[i]))
print(max(m))
