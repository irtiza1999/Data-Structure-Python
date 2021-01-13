# How to find a missing number in an integer array of 1 to 100?

# 1 + 2 + 3 + ...... + n = n(n+1)/2

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#           31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
#           58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
#           86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#
#
# def findMissing(list, n):
#     sum1 = (n * (n+1)) / 2
#     sum2 = 0
#     for item in list:
#         sum2 += item
#     if sum1 > sum2:
#         result = sum1 - sum2
#         return int(result)
#
#
# print(findMissing(mylist, 100))

# A program to find all pairs of integers whose sum is equal to a given number

# myList = [1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
#
# def similarPair(list, sum):
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] != list[j]:
#                 if (list[i] + list[j]) == sum:
#                     print(list[i], list[j])
#
#
# similarPair(myList, 20)

# Check an array if it contains a certain number or not!!
#
# import numpy as np
#
# myArray = np.array([1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#
#
# def findNumber(array, number):
#     for item in range(len(array)):
#         if array[item] == number:
#             print(f"{number} was found at index {item}.")
#             break
#     else:
#         print(f"{number} is not in the array.")
#
#
# findNumber(myArray, 50)


# Maximum product of two integers in the array where all elements are positive.

# import numpy as np
#
# myArray = np.array([1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#
#
# def findMaxProduct(array):
#     result = 0
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] * array[j] > result:
#                 result = array[i] * array[j]
#                 pairs = (f"{array[i]}, {array[j]}")
#     print(pairs)
#     print(result)
#
#
# print(findMaxProduct(myArray))


# Is the array is unique or not.

# myList = [1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
#
# def unique(list):
#     empty = []
#     for i in list:
#         if i in empty:
#             print(i)
#             print("False")
#         else:
#             empty.append(i)
#     return True
#
#
# unique(myList)


# List permutaion. Peek == Keep
#
# myList1 = [1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# myList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# def permutaion(list1, list2):
#     # reverseList2 = list2[::-1]
#     # print(reverseList2)
#     list2.reverse()
#     if list1 == list2:
#        print("True")
#     else:
#         print("False")
#
# permutaion(myList1, myList2)


# Give an image representation of a NxN matrix and write a method to rotate it by 90 degree.

import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray)


def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom -> left
            matrix[-i - 1][layer] = matrix[layer - i][-i - 1]
            # right -> bottom
            matrix[layer - i][-i - 1] = matrix[i][-layer - 1]
            # top -> right
            matrix[i][-layer - 1] = top
    return matrix


print(rotateMatrix(myArray))
