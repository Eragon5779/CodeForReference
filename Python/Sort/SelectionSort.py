def selectionsort(sortablelist):
    n = len(sortablelist)
    for j in range(n-1, 0, -1):
        posMax = 0
        for i in range(1, j+1):
            if (sortablelist[i] > sortablelist[posMax]):
                posMax = i
        temp = sortablelist[posMax]
        sortablelist[posMax] = sortablelist[j]
        sortablelist[j] = temp
