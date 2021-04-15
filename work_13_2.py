n = int(input())
lst = []
for i in range(n):
    m = int(input())
    lst.append(m)
print(*sorted(lst, reverse=True), sep='\n')
