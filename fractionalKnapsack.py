# Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit an dthe tital value is a large as possible.

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    useCapacity = 0
    totalValue = 0
    for i in items:
        if useCapacity + i.weight <= capacity:
            useCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - useCapacity
            value = i.ratio * unusedWeight
            useCapacity += unusedWeight
            totalValue += value
        if useCapacity == capacity:
            break
    print("Total: ", totalValue)


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

knapsack(cList, 100)
