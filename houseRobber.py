# Given N number of houses along the street with some ammount of money. Adjacent houses cannot be stolen. Find the maximum ammount that can be stolen.

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        steal1 = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        steal2 = houseRobber(houses, currentIndex + 1)
        return max(steal1, steal2)


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0))
