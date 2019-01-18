userString = input('Enter the string\n')
loopCount = len(userString)
stringPos = len(userString)
arrayToReturn = []
while loopCount != 0:
    loopCount = loopCount - 1
    stringPos = stringPos - 1
    arrayToReturn.append(userString[stringPos])

print(arrayToReturn)