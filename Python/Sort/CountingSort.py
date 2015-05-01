def countingsort(sortablelist):
    maxval = max(sortablelist)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in sortablelist:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            sortablelist[i] = a
            i += 1

def main():
    import random
    a = [random.randint(0, 1000) for i in range(100)]
    countingsort(a)
    print (a)

main()
