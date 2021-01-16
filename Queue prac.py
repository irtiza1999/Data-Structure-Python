class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element inserted!!"

    def dequeue(self):
        if self.isEmpty():
            return "Not valid"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Not valid"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            return "No space!!"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start == 0
            self.items[self.top] = value
            return "The element was successfully inserted!!"

    def deQueue(self):
        if self.isEmpty():
            return "No"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "No"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)

print(customQueue.deQueue())
print(customQueue.peek())
customQueue.delete()


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class LLQueue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "No element!!"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "No element!!"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        return "Deleted"


customQueue = LLQueue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())
print(customQueue.delete())


from collections import deque

customqueue = deque(maxlen=3)
customqueue.append(1)
customqueue.append(2)
customqueue.append(3)
print(customqueue)
print(customqueue.popleft())
customqueue.clear()
print(customqueue)

import queue as q

customqueue = q.Queue(maxsize=3)
print(customqueue.qsize())
print(customqueue.empty())
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.full())
print(customqueue.get())
print(customqueue.qsize())


from multiprocessing import Queue

customqueue = Queue(maxsize=3)
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.get())
