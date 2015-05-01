def bucketsort(sortablelist):
    maxval = max(sortablelist) + 1
    bucket = [[] for x in range(10)] #The three empty buckets
    #Populating the buckets with the list elements
    for i in range(len(sortablelist)):
        bucketlocal = int(sortablelist[i] / (maxval/10))
        bucket[bucketlocal].append(sortablelist[i])
    for x in bucket:
        x.sort()
    final = []
    for y in bucket:
        final += y
    return final
    #Prints the buckets and their contents

def main():
    import random
    a = [random.randint(0, 1000) for i in range(100)]
    a = bucketsort(a)
    print (a)

main()
