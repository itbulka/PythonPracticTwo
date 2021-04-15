n = input().split()
lst = []
summ = 0
for i in range(int(n[0])):
    m = input().split()
    m[1] = m[1][1:]
    m[2] = m[2][1:]
    if int(m[0])*int(m[1]) != int(m[2]):
        lst.append(i+1)
    summ += int(m[0])*int(m[1])
print(int(n[1])-summ)
print(*lst, sep=' ')
