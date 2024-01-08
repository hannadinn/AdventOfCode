colorFirstLetterDict = {
    "r": 12,
    "g": 13,
    "b": 14
}

def day2():
    file = open("day2.txt", "r")
    gameIdSum = 0
    for line in file:
        splitColon = line.split(":")
        gameId = int(splitColon[0].split(" ")[1])
        sets = [set.strip() for set in splitColon[1].split(";")]
        possibleGame = True
        for set in sets:
            listNumAndColor = set.split(", ")
            for numAndColor in listNumAndColor:
                numColorSplit = numAndColor.split(" ")
                num = int(numColorSplit[0])
                colorFirstLetter = numColorSplit[1][0]
                if (num > colorFirstLetterDict.get(colorFirstLetter)):
                    possibleGame = False
                    break
            if (possibleGame is False):
                break
        if (possibleGame is True):
            gameIdSum += gameId
    print (gameIdSum)

day2()