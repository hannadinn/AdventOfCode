numbersDict = {
"one": "1",
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9",
}

shortestWordInDictLength = len(min(numbersDict, key=len))
longestWordInDictLength = len(max(numbersDict, key=len))

file = open("day1.txt", "r")
result = 0
for line in file:
    print(len(line))
    leftIndex = 0
    rightIndex = len(line) - 2
    leftResult = leftPointer = line[leftIndex]
    # leftResult = "a"
    rightResult = rightPointer = line[rightIndex]
    # rightResult = "a"
    while (leftPointer.isalpha() and leftResult.isalpha()):
        leftAlphaStartIndex = leftIndex
        leftAlphaStart = line[leftAlphaStartIndex]
        leftTempWord = ""
        while (leftAlphaStart.isalpha() and len(leftTempWord) <= longestWordInDictLength):
            print(leftTempWord)
            leftTempWord += leftAlphaStart
            if (len(leftTempWord) >= shortestWordInDictLength):
                if leftTempWord in numbersDict:
                    leftResult = numbersDict.get(leftTempWord)
            leftAlphaStartIndex += 1
            leftAlphaStart = line[leftAlphaStartIndex]
        leftIndex += 1
        leftPointer = line[leftIndex]
        if (leftPointer.isdigit()):
            leftResult = leftPointer
    while (rightPointer.isalpha() and rightResult.isalpha()):
        rightAlphaStartIndex = rightIndex
        rightAlphaStart = line[rightAlphaStartIndex]
        rightTempWord = ""
        while (rightAlphaStart.isalpha() and len(rightTempWord) <= longestWordInDictLength):
            print(rightTempWord)
            rightTempWord += rightAlphaStart
            if(len(rightTempWord) >= shortestWordInDictLength):
                if (rightTempWord[::-1] in numbersDict):
                    rightResult = numbersDict.get(rightTempWord[::-1])
            rightAlphaStartIndex -= 1
            rightAlphaStart = line[rightAlphaStartIndex]
        rightIndex -= 1
        rightPointer = line[rightIndex]
        if (rightPointer.isdigit()):
            rightResult = rightPointer
    num = int(leftResult) * 10 + int(rightResult)
    print(num)
    result += num

print(result)
