import statistics
n = int(input())
moda, mediana = [], []
lst = []
for i in range(n):
    s = input().split()
    moda.append(statistics.mode(s))
    mediana.append(statistics.median(s))
    lst.extend(s)
print(*moda)
print(*mediana)
print(statistics.mode(moda))
print(statistics.median(mediana))
print(statistics.median(lst))
print(statistics.mode(lst))
