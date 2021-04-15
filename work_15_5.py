n = int(input())
lst = []
for i in range(n):
    s = input()
    s2 = s.split()
    if 'встал' in s or 'встала' in s:
        lst.append(s2[0])
    if 'будет за тобой' in s:
        name = s2[1][0:-1]
        j = lst.index(name)
        lst.insert(j+1, s2[2])
    if 'хватит тут стоять, пошли отсюда' in s:
        lst.remove(s2[0][0:-1])
print(*lst, sep='\n')
