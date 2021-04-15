s = input()
n = s[1::].replace('V', '!V!').split('!')
pos = 0
k = 1 if len(s) == 1 or s[1] == 'V' else 0
for i in n:
    if i == '':
        continue
    elif i[0] == '<':
        pos -= len(i)
        print(pos * ' ' + s[0] + i.replace('<', s[0]))
        k = 0
    elif i[0] == '>':
        print(pos * ' ' + s[0] + i.replace('>', s[0]))
        pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k:
            print(pos * ' ' + s[0])
        k = 1
if k:
    print(pos * ' ' + s[0])
