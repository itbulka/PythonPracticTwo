wordUser = input("Enter the word -> ")
valueUser = int(input("Enter number letter in the word -> "))
letter = input("Enter the letter ->")

if (letter == wordUser[valueUser - 1]):
    print("YES")
else:
    print("ERROR")