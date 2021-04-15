wordUser = input("Enter the word -> ")
s = list(wordUser)
sizeList = len(s) - 1
for i in range(0, int(sizeList/2)):
    print("".join(s))
    if (len(s) == 2):
        break
    del s[i]
    del s[len(s) - 1 - i]
print("".join(s))