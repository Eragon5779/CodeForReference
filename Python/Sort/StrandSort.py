def strandsort(unsorted):
    items = len(unsorted)
    sortedBins = []
    while( len(unsorted) > 0 ):
        highest = float("-inf")
        newBin = []
        i = 0
        while( i < len(unsorted) ):
            if( unsorted[i] >= highest ):
                highest = unsorted.pop(i)
                newBin.append( highest )
            else:
                i=i+1
        sortedBins.append(newBin)
    sorted = []
    while( len(sorted) < items ):
        lowBin = 0
        for j in range( 0, len(sortedBins) ):
            if( sortedBins[j][0] < sortedBins[lowBin][0] ):
                lowBin = j
        sorted.append( sortedBins[lowBin].pop(0) )
        if( len(sortedBins[lowBin]) == 0 ):
            del sortedBins[lowBin]
    return sorted
