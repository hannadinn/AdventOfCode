numCoordinatesDict = {}
symbolCoordinatesDict = {}
maxCol = 140

def day3():
    rowNum = 1
    file = open("day3.txt", "r")
    for row in file:
        fullNum = ""
        numColCoordinateList = []
        for col in range(1,len(row)+1):
            char = row[col-1]
            if (char.isdigit()):
                fullNum += char
                numColCoordinateList.append(col)
                if ((col == (len(row) + 1)) and numColCoordinateList):
                    for numColCoordinate in numColCoordinateList:
                        numCoordinatesDict[(rowNum,numColCoordinate)] = fullNum
                    fullNum = ""
                    continue
            if (numColCoordinateList):
                for numColCoordinate in numColCoordinateList:
                    numCoordinatesDict[(rowNum,numColCoordinate)] = fullNum
                fullNum = ""
                numColCoordinateList = []
            if (char != "." and char.isdigit() is False and char != "\n"):
                symbolCoordinatesDict[(rowNum,col)] = 1
        rowNum += 1
    
    partSum = 0
    for coordinates in symbolCoordinatesDict:
        coordinatesToSearchInNumsList = [
        (coordinates[0]-1,coordinates[1]-1),
        (coordinates[0]-1,coordinates[1]),
        (coordinates[0]-1,coordinates[1]+1),
        (coordinates[0],coordinates[1]-1),
        (coordinates[0],coordinates[1]+1),
        (coordinates[0]+1,coordinates[1]-1),
        (coordinates[0]+1,coordinates[1]),
        (coordinates[0]+1,coordinates[1]+1)
        ]
        for coordinatesToSearch in coordinatesToSearchInNumsList:
            tempNum = ""
            if (numCoordinatesDict.get(coordinatesToSearch, 0) != 0):
                tempNum = numCoordinatesDict.get(coordinatesToSearch)
                del numCoordinatesDict[coordinatesToSearch]
                tempNum = formTempNum(coordinatesToSearch, tempNum)
                partSum += int(tempNum)
                tempNum = ""
    print(partSum)
    print(525911)

    

def formTempNum(coordinatesToSearch, tempNum):
    for col in range(coordinatesToSearch[1]-1,0,-1):
        if (numCoordinatesDict.get((coordinatesToSearch[0],col), 0) != 0):
            tempNum = str(numCoordinatesDict.get((coordinatesToSearch[0],col))) + tempNum
            del numCoordinatesDict[(coordinatesToSearch[0],col)]
        else:
            break
    for col in range(coordinatesToSearch[1]+1,maxCol+1,1):
        if (numCoordinatesDict.get((coordinatesToSearch[0],col), 0) != 0):
            tempNum = tempNum + str(numCoordinatesDict.get((coordinatesToSearch[0],col)))
            del numCoordinatesDict[(coordinatesToSearch[0],col)]
        else:
            break
    return tempNum


day3()