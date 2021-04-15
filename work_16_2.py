n = [input().split(',') for i in range(int(input()))]
m = int(input())
lst = []
for i in range(m):
    c = input().split(',')
    print(n[int(c[0])][int(c[1])])
