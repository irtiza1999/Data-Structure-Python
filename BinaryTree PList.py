class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Found"
        return "Not found"

    def preOrderTrevarsal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTrevarsal(index * 2)
        self.preOrderTrevarsal(index * 2 + 1)

    def inOrderTrevarsal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTrevarsal(index * 2)
        print(self.customList[index])
        self.preOrderTrevarsal(index * 2 + 1)

    def postOrderTrevarsal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTrevarsal(index * 2)
        self.preOrderTrevarsal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTrevarsal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "No node to delete!!"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node deleted successfully"

    def deleteBT(self):
        self.customList = None
        return "Tree is noo more"
newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
print(newBT.deleteBT())

