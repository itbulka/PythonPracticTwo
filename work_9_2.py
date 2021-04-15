from collections import Counter
valueList = int(input("Enter value list -> "))
listStudents = [list(input("Введите фамилии в строчку ").split()) for i in range(valueList)]
newArrayToList = []
namesStudents = []

for i in range(valueList):
    for j in range(len(listStudents[i])):
        newArrayToList.append(listStudents[i][j])

listCounter = Counter(newArrayToList)
namesStudents = list(listCounter)

for i in range(len(namesStudents)):
    if (listCounter[namesStudents[i]] == valueList):
        print(namesStudents[i])