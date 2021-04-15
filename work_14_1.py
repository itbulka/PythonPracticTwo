n = int(input())
lst = []
for i in range(n):
    s = input()
    if 'лук' not in s:
        lst.append(s)
print(*lst, sep=', ')
