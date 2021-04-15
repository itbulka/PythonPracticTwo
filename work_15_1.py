b = input()
s = input().split()
for i in range(len(s)):
    if b.lower() in s[i] or b.upper() in s[i]:
        print(s[i])
    else:
        continue
