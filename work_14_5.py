s = input().split('&')
key = input()
for i in range(len(s)):
    if key in s[i]:
        c = s[i]
        print(c[c.find('=')+1:])
    else:
        continue
