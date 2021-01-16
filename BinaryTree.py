# class TreeNode:
#     def __init__(self, data, children=[]):
#         self.data = data
#         self.children = children
#
#     def __str__(self, level=0):
#         ret = ' ' * level + str(self.data) + '\n'
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret
#
#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)
#
# tree = TreeNode("Driks", [])
# cold = TreeNode("Cold", [])
# hot = TreeNode("Hot", [])
#
# tea = TreeNode("Tea", [])
# coffee = TreeNode("coffee", [])
#
# cola = TreeNode("Cola", [])
# fanta = TreeNode("Fanta", [])
#
# tree.addChild(cold)
# tree.addChild(hot)
# cold.addChild(cola)
# cold.addChild(fanta)
# hot.addChild(tea)
# hot.addChild(coffee)
# print(tree)

import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drkinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTravarsal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTravarsal(rootNode.leftChild)
    preOrderTravarsal(rootNode.rightChild)


def inOrderTreversal(rootNode):
    if not rootNode:
        return
    inOrderTreversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTreversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTreversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Bt does not exist!!"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return (nodeValue, "founded")
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Value is not in BT!!"


def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Insert in left"
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Insert in right"

newNode = TreeNode("Cola")
newNode2 = TreeNode("Black Coffee")
print(insertBT(newBT, newNode))
print(insertBT(newBT, newNode2))
levelOrderTreversal(newBT)