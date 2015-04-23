def quicksort (sortablelist):
    '''Quick sorts the list must print the list after done sorting'''
    output = quicksorthelper(sortablelist, 0, len(sortablelist) - 1)

def quicksorthelper (sortablelist, first, last):
    '''Called in a recursive fashion'''
    temp = []
    if first < last:
        middle = partition(sortablelist, first, last)
        
        quicksorthelper(sortablelist, first, middle - 1)
        quicksorthelper(sortablelist, middle + 1, last)

def partition(sortablelist, first, last):
    pivotpoint = sortablelist[first]

    left = first + 1
    right = last

    while True:
        while left <= right and sortablelist[left] <= pivotpoint:
            left += 1

        while right >= left and sortablelist[right] >= sortablelist[left]:
            right -= 1

        if right < left:
            break

        else:
            temp = sortablelist[left]
            sortablelist[left] = sortablelist[right]
            sortablelist[right] = temp

    temp = sortablelist[first]
    sortablelist[first] = sortablelist[right]
    sortablelist[right] = temp

    return right
