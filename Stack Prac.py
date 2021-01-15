# class Stack:
#     def __init__(self, maxSize):
#         self.list = []
#         self.maxSize = maxSize
#
#     def __str__(self):
#         values = self.list.reverse()
#         values = (str(x) for x in self.list)
#         return '\n'.join(values)
#
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#
#     def isFull(self):
#         if len(self.list) == self.maxSize:
#             return True
#         else:
#             return False
#
#     def push(self, value):
#         if self.isFull():
#             return "The stack is full!!"
#         else:
#             self.list.append(value)
#             return "Element added!!"
#
#     def pop(self):
#         if self.isEmpty():
#             return "There is no element in the stack!!"
#         else:
#             return self.list.pop()
#
#     def peek(self):
#         if self.isEmpty():
#             return "There is no element in the stack!!"
#         else:
#             return self.list[(len(self.list) - 1)]
#
#     def delete(self):
#         self.list = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class LLStack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "No"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "No"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None
        return "Deleted"

customStack = LLStack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.delete())
