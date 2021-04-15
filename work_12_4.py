s = input()
c, c1 = 0, 0
m = 0
for i in range(len(s)):
    a = s.find('0')
    b = s.find('1')
    if a != -1 and b != -1:
        if s[0] == '0':
            print(b-a, s[0])
            s = s[b:len(s)]
        elif s[0] == '1':
            print(a-b, s[0])
            s = s[a:len(s)]
        else:
            break
    else:
        if '1' in s:
            m = 1
            c1 = s.count('1')
        else:
            m = 0
            c = s.count('0')
if m == 1:
    print(c1, m)
else:
    print(c, m)
