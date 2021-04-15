lst = {}
for i in range(int(input())):
    value, key = input().split()
    if key in lst:
        lst[key].append(value)
    else:
        lst[key] = [value]
for j in range(int(input())):
    key = input()
    print(*lst.get(key, ['Нет в телефонной книге']))
