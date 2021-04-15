n = int(input())
c, j, y = 0, 0, 0
k, k1 = 0, 0
for i in range(n):
    s = input()
    while s[j] == ' ':
        c += 1
        j += 1
    s = s.split()
    s = ' '.join(s)
    s = ' ' * c + s
    k = s.find("'")
    k1 = s.rfind("'")
    if '#' in s:
        for x in range(len(s)):
            if s[x] == '#':
                if x < k or x > k1:
                    y = x
                else:
                    y = len(s)
        print(s[0:y])
    else:
        print(s)
