#dx = int(input("Desplazamient en x: "))
#dy = int(input("Desplazamient en y: "))

input = open("Day3_TobogganTrajectory\\input.txt")
data = input.read().splitlines()

tree = '#'
posX = [0,0,0,0,0]
posY = [0,0,0,0,0]
dx = [1,3,5,7,1]
dy = [1,1,1,1,2]
count = [0,0,0,0,0]
completed = 0
while completed < len(posX):
    for i in range(0,len(posX)):
        if posY[i] < len(data):
            if data[posY[i]][posX[i]%len(data[posY[i]])] == tree:
                count[i] += 1
            posX[i] += dx[i]
            posY[i] += dy[i]
            completed = 0
            for number in posY:
                if number >= len(data):
                    completed += 1
print("Number of trees encounted: ", count)
result = 1
for numberOfTress in count:
    result = result * numberOfTress
print("Result of multiplication", result)
