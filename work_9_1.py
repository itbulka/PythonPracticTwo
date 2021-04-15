numberBooksLibery = int(input("Enter number books in the library -> "))
numberBooksUser = int(input("Enter number books -> "))

arrayBooksLibrary = [input("Enter name book") for i in range(numberBooksLibery)]
arrayBooksUser = [input("Enter name book user") for i in range(numberBooksUser)]

for i in range(numberBooksLibery):
    for j in range(numberBooksUser):
        if (arrayBooksUser[j] == arrayBooksLibrary[i]):
            print(f"{arrayBooksUser[j]} YES")
