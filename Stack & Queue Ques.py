# #  How to use a single Python list to implement three stacks
#
# class MultiStack:
#     def __init__(self, stacksize):
#         self.numberstacks = 3
#         self.cuslist = [0] * (stacksize * self.numberstacks)
#         self.sizes = [0] * self.numberstacks
#         self.stacksize = stacksize
#
#     def isFull(self, stacknum):
#         if self.sizes[stacknum] == self.stacksize:
#             return True
#         else:
#             return False
#
#     def isEmpty(self, stacknum):
#         if self.sizes[stacknum] == 0:
#             return True
#         else:
#             return False
#
#     def indexOfTop(self, stacknum):
#         offset = stacknum * self.stacksize
#         return offset + self.sizes[stacknum] - 1
#
#     def push(self, item, stacknum):
#         if self.isFull(stacknum):
#             return "Stack is full"
#         else:
#             self.sizes[stacknum] += 1
#             self.cuslist[self.indexOfTop(stacknum)] = item
#
#     def pop(self, stacknum):
#         if self.isEmpty(stacknum):
#             return "Stack is empty"
#         else:
#             value = self.cuslist[self.indexOfTop(stacknum)]
#             self.cuslist[self.indexOfTop(stacknum)] = 0
#             self.sizes[stacknum] -= 1
#             return value
#
#     def peek(self, stacknum):
#         if self.isEmpty(stacknum):
#             return "Stack is empty"
#         else:
#             value = self.cuslist[self.indexOfTop(stacknum)]
#             return value
#
#
# customstack = MultiStack(6)
#
# print(customstack.isFull(0))
# print(customstack.isEmpty(1))
# customstack.push(1, 0)
# customstack.push(2, 0)
# customstack.push(3, 2)
# print(customstack)
# print(customstack.peek(1))

#   Create Stack with min method

# class Node():
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         string = str(self.value)
#         if self.next:
#             string += "," + str(self.next)
#         return string
#
#
# class Stack():
#     def __init__(self):
#         self.top = None
#         self.minNode = None
#
#     def min(self):
#         if not self.minNode.value:
#             return None
#         else:
#             return self.minNode.value
#
#     def push(self, item):
#         if self.minNode and (self.minNode.value < item):
#             self.minNode = Node(value=self.minNode.value, next=self.minNode)
#         else:
#             self.minNode = Node(value=item, next=self.minNode)
#         self.top = Node(value=item, next=self.top)
#
#     def pop(self):
#         if not self.top:
#             return None
#         self.minNode = self.minNode.next
#         item = self.top.value
#         self.top = self.top.next
#         return item
#
#
# customstack = Stack()
#
# customstack.push(99)
# customstack.push(-1)
# customstack.push(1)
# customstack.push(8)
# customstack.push(7)
# customstack.push(5)
# customstack.push(-100)
# customstack.pop()
# print(customstack.min())

# Implement Queue class which implements a queue using two stacks.

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class QueueViaStack():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())