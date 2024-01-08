numbersDict = [
"one": 1,

]

file = open("day1.txt", "r")
result = 0
for line in file:
    print(len(line))
    leftIndex = 0
    rightIndex = len(line) - 2
    leftDigit = line[leftIndex]
    rightDigit = line[rightIndex]
    print(leftDigit)
    print(rightDigit)
    while (leftDigit.isalpha()):
        print(leftDigit)
        leftIndex+=1
        leftDigit = line[leftIndex]
    while (rightDigit.isalpha()):
        print(rightDigit)
        rightIndex-=1
        rightDigit = line[rightIndex]
    num = int(leftDigit) * 10 + int(rightDigit)
    print(num)
    result += num

print(result)
