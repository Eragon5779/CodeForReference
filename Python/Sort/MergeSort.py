import math

def MergeSort(sortableList):
    length = len(sortableList)
    left = []
    right = []
    if (length <= 1):
        return sortableList
    for x in range(0, math.ceil(length/2)):
        left.append(sortableList[x])
    left = MergeSort(left)
    for y in range(math.ceil(length/2), length):
        right.append(sortableList[y])
    right = MergeSort(right)
    sortableList = Merge(left, right)
    return sortableList

def Merge(left, right):
    sortableList = []
    while (len(left) != 0 and len(right) != 0):
        if (left[0] < right[0]):
            sortableList.append(left.pop(0))
        else:
            sortableList.append(right.pop(0))
    while (len(left) != 0):
        sortableList.append(left.pop(0))
    while (len(right) != 0):
        sortableList.append(right.pop(0))
    return sortableList
