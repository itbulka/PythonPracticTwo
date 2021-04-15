wordUser = input("Enter 'o' or 'р'")
array = wordUser.split('р')
maxValue = 0

for i in range(len(array)):
    symbol = array[i]
    if (len(symbol) > maxValue):
        maxValue = len(symbol)
        
print(maxValue)