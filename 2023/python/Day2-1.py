colorFirstLetterDict = {
    "r": 0,
    "g": 0,
    "b": 0
}

def day2_1():
    file = open("day2.txt", "r")
    setsSum = 0
    for line in file:
        splitColon = line.split(":")
        sets = [set.strip() for set in splitColon[1].split(";")]
        for set in sets:
            listNumAndColor = set.split(", ")
            for numAndColor in listNumAndColor:
                numColorSplit = numAndColor.split(" ")
                num = int(numColorSplit[0])
                colorFirstLetter = numColorSplit[1][0]
                if (num > colorFirstLetterDict.get(colorFirstLetter)):
                    colorFirstLetterDict[colorFirstLetter] = num
        colorList = list(colorFirstLetterDict.values())
        setSum = 1
        for color in colorList:
            setSum *= color
        setsSum += setSum
        setSum = 1
        colorFirstLetterDict["r"] = 0
        colorFirstLetterDict["g"] = 0
        colorFirstLetterDict["b"] = 0
    print (setsSum)

day2_1()