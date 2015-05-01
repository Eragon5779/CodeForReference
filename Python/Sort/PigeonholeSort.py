def pigeonholesort(sortablelist):
    my_min = min(sortablelist)
    my_max = max(sortablelist)
    size = my_max - my_min + 1
    holes = [0] * size
    for x in sortablelist:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            sortablelist[i] = count + my_min
            i += 1

def main():
    import random
    a = [random.randint(0, 1000) for i in range(100)]
    pigeonholesort(a)
    print (a)

main()
