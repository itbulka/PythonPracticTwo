s = input()
c, m, n = 0, 0, 0
F, f = False, False
lst = [0] * 30000
for i in s:
    if i == '[':
        f = True
        m += 1
    elif i == ']':
        n += 1
    if m - n > 0:
        if i == '+' and lst[c] != 0:
            lst[c] += 1
        elif i == '-' and lst[c] != 0:
            while lst[c] != 0:
                lst[c] -= 1
                lst[c] = lst[c] % 256
    elif i == '>':
        c += 1
    elif i == '<':
        c -= 1
    elif i == '+':
        lst[c] += 1
    elif i == '-':
        lst[c] -= 1
        lst[c] = lst[c] % 256
    elif i == '.':
        print(lst[c])
