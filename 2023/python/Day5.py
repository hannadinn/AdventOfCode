seedsToEntityDict = {}

def day5():
    file = open("day5.txt", "r")
    entityList = (file.readline().split(":"))[1].strip().split(" ")
    file.readline()

    # start processing on 3rd line onwards
    addToMap = False
    mapOrder = 1
    for row in file:
        # process on blank row
        if (len(row) == 1):
            entityList = mapListWithNewEntity(entityList)
            print(entityList)
            addToMap = False
            mapOrder = 1
            seedsToEntityDict.clear()
            continue
        if (addToMap is True):
            entityRangeCombiList = row.strip().split(" ")
            lowerBound = int(entityRangeCombiList[1])
            upperBound = int(entityRangeCombiList[1]) + int(entityRangeCombiList[2]) - 1
            mappedEntity = int(entityRangeCombiList[0])
            seedsToEntityDict[mapOrder] = [lowerBound,upperBound,mappedEntity]
            mapOrder += 1
        if (row[-2] == ":"):
            addToMap = True
    entityList = mapListWithNewEntity(entityList)
    print(min(entityList))



def mapListWithNewEntity(entityList):
    print(seedsToEntityDict)
    newEntityList = []
    for entity in entityList:
        newEntity = int(entity)
        entityMatched = False
        for mapOrder, newEntityCombi in sorted(seedsToEntityDict.items()):
            if (entityMatched is True):
                break
            else:
                lowerBound = newEntityCombi[0]
                upperBound = newEntityCombi[1]
                mappedEntity = newEntityCombi[2]
                if (int(newEntity) >= lowerBound and int(newEntity) <= upperBound):
                    newEntity = int(newEntity) - lowerBound + mappedEntity
                    entityMatched = True
        newEntityList.append(int(newEntity))
    return newEntityList



day5()