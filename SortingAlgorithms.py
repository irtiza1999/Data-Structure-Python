# Bubble sort

def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


# Selection Sort

def selectionSort(customList):
    for i in range(len(customList)):
        min = i
        for j in range(i + 1, len(customList)):
            if customList[min] > customList[j]:
                min = j
        customList[i], customList[min] = customList[min], customList[i]
    print(customList)


# Insertion Sort

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)


list1 = [5, 4, 3, 2, 1, 100, -100]
insertionSort(list1)
