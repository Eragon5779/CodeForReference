def combsort(sortablelist):
    gap = len(sortablelist)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(sortablelist) - gap):
            j = i+gap
            if sortablelist[i] > sortablelist[j]:
                sortablelist[i], sortablelist[j] = sortablelist[j], sortablelist[i]
                swaps = True
