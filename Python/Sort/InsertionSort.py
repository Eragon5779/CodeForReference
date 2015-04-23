def insertionsort(sortablelist):
    '''Insertion sorts a list of numbers'''
    for index in range(1, len(sortablelist)):
        currentvalue = sortablelist[index]
        position = index
        while position > 0 and sortablelist[position - 1] > currentvalue:
            sortablelist[position] = sortablelist[position - 1]
            position -= 1
        sortablelist[position] = currentvalue
    print(sortablelist)
