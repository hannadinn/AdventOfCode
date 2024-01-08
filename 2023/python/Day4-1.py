winningCardsDict = {}
scratchCardsCountDict = {}

def day4():
    rowNum = 1
    file = open("day4.txt", "r")
    for row in file:
        addToScratchCardCount(rowNum, 1)
        cards = row.split(":")[1]
        winningCardsList = cards.split("|")[0].strip().split(" ")
        actualCardsList = cards.split("|")[1].strip().split(" ")
        for winningCard in winningCardsList:
            if (winningCard != ""):
                winningCardsDict[winningCard] = 1
        cardMatches = 0
        for actualCard in actualCardsList:
            if (actualCard == ""):
                continue
            if (winningCardsDict.get(actualCard) is not None):
                cardMatches += 1
        cardNumWonList = createCardNumWonList(rowNum, cardMatches)
        scratchCardCountForCurrentRow = scratchCardsCountDict.get(rowNum)
        for cardNum in cardNumWonList:
            addToScratchCardCount(cardNum, scratchCardCountForCurrentRow)
        winningCardsDict.clear()
        rowNum += 1
    print(sum(scratchCardsCountDict.values()))



def addToScratchCardCount(rowNum, cardsToAdd):
    if (scratchCardsCountDict.get(rowNum) is None):
        scratchCardsCountDict[rowNum] = cardsToAdd
    else:
        scratchCardsCountDict.update({rowNum: int(scratchCardsCountDict.get(rowNum)) + cardsToAdd})



def createCardNumWonList(rowNum, cardMatches):
    cardNumWonList = []
    for cardNum in range(1, cardMatches + 1):
        cardNumWonList.append(rowNum + cardNum)
    return cardNumWonList



day4()