dx = int(input("Desplazamient en x: "))
dy = int(input("Desplazamient en y: "))

input = open("Day3_TobogganTrajectory\\input.txt")
inputList = input.read().splitlines()
tree = '#'
posX = 0
posY = 0
counter = 0
for row in inputList:
    if(row[posX % len(row)] == tree):
        counter += 1
    posX += dx
    posY += dy
print("Number of trees encounted: ", counter)
