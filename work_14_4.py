n = input().split()
n2 = [int(n[i]) for i in range(len(n))]
x = len(n2)
y = max(n2)
print('*' * (x + 2))
print('*' + ' ' * x + '*')
for j in range(1, y+1):
    print(end='*')
    for i in n2:
        if i >= y - j + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')
