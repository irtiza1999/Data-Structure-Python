class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSingle(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSingle(self):
        if self.head is None:
            print("List does not have any element!!")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" ")
                node = node.next

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "List does not exists!!"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value is not in the List!!"

    def deleteNode(self, location):
        if self.head is None:
            print("The list does not exists!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteAll(self):
        if self.head is None:
            print("Does not exxits!!")
        else:
            self.head = None
            self.tail = None
            print("Deleted")

singlyLinkedList = SingleLinkedList()
node = Node()
singlyLinkedList.insertSingle(1, 0)
singlyLinkedList.insertSingle(2, 1)
singlyLinkedList.insertSingle(3, 1)
singlyLinkedList.insertSingle(4, 1)
output = (list(node.value for node in singlyLinkedList))
print(output)
singlyLinkedList.deleteNode(0)
print(list(node.value for node in singlyLinkedList))
singlyLinkedList.deleteAll()
print(list(node.value for node in singlyLinkedList))