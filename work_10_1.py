word = input("Enter the word -> ")
value = int(input("Enter the letter number in the word -> "))

try:
    print(word[value - 1])
except:
    print("Out-of-range number!")