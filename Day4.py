winningCardsDict = {}

def day4():
    totalPoints = 0
    file = open("day4.txt", "r")
    for row in file:
        cards = row.split(":")[1]
        winningCardsList = cards.split("|")[0].strip().split(" ")
        actualCardsList = cards.split("|")[1].strip().split(" ")
        for winningCard in winningCardsList:
            if (winningCard != ""):
                winningCardsDict[winningCard] = 1
        winCardCount = 0
        for actualCard in actualCardsList:
            if (actualCard == ""):
                continue
            if (winningCardsDict.get(actualCard) is not None):
                winCardCount += 1
        totalPoints += power(winCardCount)
        winningCardsDict.clear()
    print(totalPoints)



def power(winCardCount):
    # 0 --> 0 
    # 1 --> 1 (2 power 0)
    # 2 --> 2 (2 power 1)
    # 3 --> 4 (2 power 2)
    result = 2
    if (winCardCount == 0):
        return 0
    elif (winCardCount == 1):
        return 1
    elif (winCardCount == 2):
        return 2
    else:
        for i in range(2, winCardCount, 1):
            result *= 2
        return result



day4()