# SSL
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
#
# class SingleLinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
#
#     def insertSingle(self, value, location):
#         newNode = Node(value)
#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             if location == 0:
#                 newNode.next = self.head
#                 self.head = newNode
#             elif location == 1:
#                 newNode.next = None
#                 self.tail.next = newNode
#                 self.tail = newNode
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 nextNode = tempNode.next
#                 tempNode.next = newNode
#                 newNode.next = nextNode
#
#     def traverseSingle(self):
#         if self.head is None:
#             print("List does not have any element!!")
#         else:
#             node = self.head
#             while node is not None:
#                 print(node.value, end=" ")
#                 node = node.next
#
#     def searchSLL(self, nodeValue):
#         if self.head is None:
#             return "List does not exists!!"
#         else:
#             node = self.head
#             while node is not None:
#                 if node.value == nodeValue:
#                     return node.value
#                 node = node.next
#             return "The value is not in the List!!"
#
#     def deleteNode(self, location):
#         if self.head is None:
#             print("The list does not exists!!")
#         else:
#             if location == 0:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     self.head = self.head.next
#             elif location == 1:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     node = self.head
#                     while node is not None:
#                         if node.next == self.tail:
#                             break
#                         node = node.next
#                     node.next = None
#                     self.tail = None
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 nextNode = tempNode.next
#                 tempNode.next = nextNode.next
#
#     def deleteAll(self):
#         if self.head is None:
#             print("Does not exxits!!")
#         else:
#             self.head = None
#             self.tail = None
#             print("Deleted")
#
# singlyLinkedList = SingleLinkedList()
# node = Node()
# singlyLinkedList.insertSingle(1, 0)
# singlyLinkedList.insertSingle(2, 1)
# singlyLinkedList.insertSingle(3, 1)
# singlyLinkedList.insertSingle(4, 1)
# output = (list(node.value for node in singlyLinkedList))
# print(output)
# singlyLinkedList.deleteNode(0)
# print(list(node.value for node in singlyLinkedList))
# singlyLinkedList.deleteAll()
# print(list(node.value for node in singlyLinkedList))


# Circular SLL
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
#
# class CircularSLL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
#             if node == self.tail.next:
#                 break
#             node = node.next
#
#     def createCSLL(self, nodeValue):
#         node = Node(nodeValue)
#         node.next = node
#         self.head = node
#         self.tail = node
#         return "The CSLL has been created."
#
#     def insertOne(self, value, loaction):
#         if self.head is Node:
#             return "The head ref is none."
#         else:
#             newNode = Node(value)
#             if loaction == 0:
#                 newNode.next = self.head
#                 self.head = newNode
#                 self.tail.next = newNode
#             elif loaction == 1:
#                 newNode.next = self.tail.next
#                 self.tail.next = newNode
#                 self.tail = newNode
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < loaction - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 nextNode = tempNode.next
#                 tempNode.next = newNode
#                 newNode.next = nextNode
#             return "Success!!"
#
#     def traversalCSLL(self):
#         if self.head is None:
#             print("No element!")
#         else:
#             tempNode = self.head
#             while tempNode:
#                 print(tempNode.value, end=" ")
#                 tempNode = tempNode.next
#                 if tempNode == self.tail.next:
#                     break
#
#     def search(self, nodeValue):
#         if self.head is None:
#             return "There is no node!!"
#         else:
#             tempNode = self.head
#             while tempNode:
#                 if tempNode.value == nodeValue:
#                     return tempNode.value
#                 tempNode = tempNode.next
#                 if tempNode == self.tail.next:
#                     return "The node does not exists!!"
#
#     def deleteNode(self, location):
#         if self.head is None:
#             print("No head is here!!")
#         else:
#             if location == 0:
#                 if self.head == self.tail:
#                     self.head.next = None
#                     self.head = None
#                     self.tail = None
#                 else:
#                     self.head = self.head.next
#                     self.tail.next = self.head
#             elif location == 1:
#                 if self.head == self.tail:
#                     self.head.next = None
#                     self.head = None
#                     self.tail = None
#                 else:
#                     node = self.head
#                     while node is not None:
#                         if node.next == self.tail:
#                             break
#                         node = node.next
#                     node.next = self.head
#                     self.tail = node
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 nextNode = tempNode.next
#                 tempNode.next = nextNode.next
#
#     def deleteAll(self):
#         if self.head is None:
#             print("No head is here!!")
#         else:
#             self.head = None
#             self.tail.next = None
#             self.tail = None
#
#
# circularSLL = CircularSLL()
# circularSLL.createCSLL(6)
# circularSLL.insertOne(1, 1)
# circularSLL.insertOne(2, 2)
# circularSLL.insertOne(3, 3)
# circularSLL.insertOne(4, 4)
# circularSLL.insertOne(4, 5)
# circularSLL.insertOne(4, 6)
# print(list(node.value for node in circularSLL))
# circularSLL.deleteAll()
# print(list(node.value for node in circularSLL))


# Doubly Linked List

class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class DoublySLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDSLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print("DSLL created!!")

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node can not be inserted!!")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def treversalDSLL(self):
        if self.head is None:
            print("No DSLL!!")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value, end=" ")
                tempNode = tempNode.next

    def reverseDSLL(self):
        if self.head is None:
            print("No emelmets!!")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value, end=" ")
                tempNode = tempNode.prev

    def searchNode(self, nodeValue):
        if self.head is None:
            print("No elements!!")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value

                tempNode = tempNode.next
            return "Node not in list!!"

    def deleteNode(self, location):
        if self.head is None:
            print("No elemet in list!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
                print("Success..")

    def deleteAll(self):
        if self.head is None:
                print("No head is here!!")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("Deleted!!")

doublySLL = DoublySLL()
doublySLL.createDSLL(1)
print(list(node.value for node in doublySLL))
doublySLL.insertNode(2, 0)
doublySLL.insertNode(3, 1)
doublySLL.insertNode(4, 1)
print(list(node.value for node in doublySLL))
print(doublySLL.deleteNode(-1))
print(list(node.value for node in doublySLL))
doublySLL.deleteAll()
print(list(node.value for node in doublySLL))