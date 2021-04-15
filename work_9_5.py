m = [input() for i in range(int(input()))]
n = int(input())
lst = list()
while n != 0:
    c = int(input())
    for i in range(c):
        s = input()
        lst.append(s)
    n -= 1
for i in range(len(m)):
    if m[i] not in lst:
        print(m[i])
#спросить насчёт произвольного порядка