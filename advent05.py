with open("input05.txt") as f:
    lines = f.readlines()

startCoordinates = []
endCoordinates = []
largestX = 0
largestY = 0

# parse the lines to coordinates
for line in lines:
    comma = line.index(",")
    startX = int(line[:comma])
    space = line.index(" ")
    startY = int(line[comma+1:space])
    line = line[space+4:-1]
    comma = line.index(",")
    endX = int(line[:comma])
    endY = int(line[comma+1:])
    startCoordinates.append([startX, startY])
    endCoordinates.append([endX, endY])
    largestX = max(largestX, startX, endX)
    largestY = max(largestY, startY, endY)

# create empty map
coordinates = [[0 for x in range(largestY+1)] for y in range(largestX+1)]

# for horizontal and vertical lines
counter1 = 0

# for diagonal lines
counter2 = 0
for i in range(len(startCoordinates)):
    startX = min(startCoordinates[i][0], endCoordinates[i][0])
    endX = max(startCoordinates[i][0], endCoordinates[i][0])
    startY = min(startCoordinates[i][1], endCoordinates[i][1])
    endY = max(startCoordinates[i][1], endCoordinates[i][1])

    if startCoordinates[i][0] == endCoordinates[i][0]:
        while startY <= endY:
            coordinates[startX][startY] += 1
            if coordinates[startX][startY] == 2:
                counter1 += 1
            startY += 1
    elif startCoordinates[i][1] == endCoordinates[i][1]:
        while startX <= endX:
            coordinates[startX][startY] += 1
            if coordinates[startX][startY] == 2:
                counter1 += 1
            startX += 1
print("Part 1: " + str(counter1))

for i in range(len(startCoordinates)):
    startX = startCoordinates[i][0]
    endX = endCoordinates[i][0]
    startY = startCoordinates[i][1]
    endY = endCoordinates[i][1]

    if startCoordinates[i][0] != endCoordinates[i][0] and startCoordinates[i][1] != endCoordinates[i][1]:
        if startY <= endY:
            while startY <= endY:
                coordinates[startX][startY] += 1
                if coordinates[startX][startY] == 2:
                    counter2 += 1
                if startY <= endY:
                    startY += 1
                else:
                    startY -= 1
                if startX <= endX:
                    startX += 1
                else:
                    startX -= 1
        else:
            while startY >= endY:
                coordinates[startX][startY] += 1
                if coordinates[startX][startY] == 2:
                    counter2 += 1
                if startY >= endY:
                    startY -= 1
                else:
                    startY += 1
                if startX >= endX:
                    startX -= 1
                else:
                    startX += 1

print("Part 2: " + str(counter1 + counter2))
