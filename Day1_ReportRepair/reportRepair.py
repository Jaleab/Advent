# Day 1 : Report Repair

input = open("Day1_ReportRepair\inputRepair.txt")
inputList = input.read().split()
numbers = []
for x in inputList:
    numbers.append(int(x.strip('\n')))
print(numbers)
solution = 0
for x in numbers:
    numberNeeded = 2020 - x
    if numberNeeded in numbers:
        solution = numberNeeded
        print(x*numberNeeded)
        break