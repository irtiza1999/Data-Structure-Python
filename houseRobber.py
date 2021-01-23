# Given N number of houses along the street with some ammount of money. Adjacent houses cannot be stolen. Find the maximum ammount that can be stolen.

# Divide and conqure
def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        steal1 = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        steal2 = houseRobber(houses, currentIndex + 1)
        return max(steal1, steal2)


# Top Down]
def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirst = houses[currentIndex] + houseRobberTD(houses, currentIndex + 2, tempDict)
            skipFirst = houseRobberTD(houses, currentIndex + 1, tempDict)
            tempDict[currentIndex] = max(stealFirst, skipFirst)
        return tempDict[currentIndex]


def houseRobberBU(houses, currentIndex):
    tempArr = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        tempArr[i] = max(houses[i] + tempArr[i+2], tempArr[i+1])
    return tempArr[0]

houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobberBU(houses, 0))
