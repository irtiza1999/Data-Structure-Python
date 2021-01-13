# Making General classes
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


# --------------------------xxxxxxx------------------------------


# Remove duplicate form a Linked List
# def removeDuplicates(ll):
#     if ll.head is None:
#         return
#     else:
#         currentNode = ll.head
#         visited = set([currentNode.value])
#         while currentNode.next:
#             if currentNode.next.value in visited:
#                 currentNode.next = currentNode.next.next
#             else:
#                 visited.add(currentNode.next.value)
#                 currentNode = currentNode.next
#         return ll
#
# def removeDupMethod2(ll):
#     if ll.head is None:
#         return
#     else:
#         currentNode = ll.head
#         while currentNode:
#             runner = currentNode
#             while runner.next:
#                 if runner.next.value == currentNode.value:
#                     runner.next = runner.next.next
#                 else:
#                     runner = runner.next
#             currentNode = currentNode.next
#         return ll.head
#
#
# customLL = LinkedList()
# customLL.generate(10, 10, 20)
# print(customLL)
# removeDupMethod2(customLL)
# print(customLL)


# Return nth Node form the Last

# def nthFromLast(ll, n):
#     pointer1 = ll.head
#     pointer2 = ll.head
#
#     for i in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next
#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1
#
#
# customLL = LinkedList()
# customLL.generate(10, 10, 20)
# print(customLL)
# print(nthFromLast(customLL, 10))


# Write a code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
#
# def partition(ll, x):
#     currNode = ll.head
#     ll.tail = ll.head
#     while currNode:
#         nextNode = currNode.next
#         currNode.next = None
#         if currNode.value < x:
#             currNode.next = ll.head
#             ll.head = currNode
#         else:
#             ll.tail.next = currNode
#             ll.tail = currNode
#         currNode = nextNode
#     if ll.tail.next is not None:
#         ll.tail.next = None
#
# customLL = LinkedList()
# customLL.generate(3, 10, 15)
# print(customLL)
# partition(customLL, 12)
# print(customLL)

# You have two numbers represemted by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

# def sumList(llA, llB):
#     n1 = llA.head
#     n2 = llB.head
#     carry = 0
#     ll = LinkedList()
#     while n1 or n2:
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         ll.add(int(result % 10))
#         carry = result / 10
#     return ll
#
#
# llA = LinkedList()
# llA.add(7)
# llA.add(3)
# llA.add(2)
#
# llB = LinkedList()
# llB.add(7)
# llB.add(3)
# llB.add(2)
#
# print(llA)
# print(llB)
# print(sumList(llA, llB))


# Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That sum of the kth node of the first linked list is the exact same node  as the jth node of the second linked list, then they are intersecting.

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 1)


print(llA)
print(llB)

print(intersection(llA, llB))
