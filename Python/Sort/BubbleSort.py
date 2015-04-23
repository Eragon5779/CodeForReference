def BubbleSort(sortableList):
    '''Bubble sorts a list of numbers'''
    length = len(sortableList)
    while True:
        swapped = 0
        for i in range(0, length-1):
            if (sortableList[i] > sortableList[i+1]):
                sortableList[i],sortableList[i+1] = sortableList[i+1],sortableList[i]
                swapped = 1
        if (swapped == 0):
            break
    return sortableList
