def sort(sortablelist):
    pos = 0
    while True:
        if (pos == 0):
            pos += 1
        if pos >= len(sortablelist):
            break
        if sortablelist[pos] >= sortablelist[pos - 1]:
            pos += 1
        else:
            sortablelist[pos - 1], sortablelist[pos] = sortablelist[pos], sortablelist[pos - 1]
            pos -= 1
