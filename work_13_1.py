n = int(input())
lst = ['']*n
for i in range(n):
    lst[i] = input()
k = int(input())
for y in range(k):
    t = int(input())
    tmp = [''] * t
    for j in range(t):
        tmp[j] = lst[int(input()) - 1]
    lst = tmp
for x in range(len(lst)):
    print(lst[x])
