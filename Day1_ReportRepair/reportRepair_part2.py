# Day 1 : Report Repair

input = open("Day1_ReportRepair\inputRepair.txt")
inputList = input.read().split()
numbers = []
for x in inputList:
    numbers.append(int(x.strip('\n')))
#print(numbers)
solution = []
solutionFound = False
for x in numbers:
    for y in numbers:
        number2Needed = 2020 - x - y
        if number2Needed in numbers:
            solution.append(x)
            solution.append(y)
            solution.append(number2Needed)
            print(solution[0]*solution[1]*solution[2])
            solutionFound = True
            break
    if(solutionFound == True):
        break