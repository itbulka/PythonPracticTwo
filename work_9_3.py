from collections import Counter
sizeName = int(input("Enter size array -> "))
firstNames = [input("Enter name -> ") for i in range(sizeName)]
count = 0

test = Counter(firstNames)
arr = list(test)

for i in range(len(arr)):
    if (test[arr[i]] > 1):
        count += test[arr[i]]

print(count)