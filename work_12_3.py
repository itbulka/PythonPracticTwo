n = int(input())
lst1, lst2 = [], []
for i in range(n):
    s = input()
    a = int(input())
    lst1.append(s)
    lst2.append(a)
lst1.reverse()
lst2.reverse()
for j in range(n):
    print(lst1[j], lst2[j])