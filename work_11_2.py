n = int(input())
lst =[]
for i in range(n):
    s = input()
    if s.startswith('%%'):
        s = s[2:-1]
    if not s.startswith('####'):
        lst.append(s)
print(*lst, sep='\n')
