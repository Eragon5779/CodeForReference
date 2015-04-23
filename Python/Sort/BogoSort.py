from random import *

def bogosort(sortablelist):
    '''Shuffles till in order'''
    while not inorder(sortablelist):
        shuffle(sortablelist)
    print(sortablelist)

def inorder(sortablelist):
    '''Checks to see if the list is in order'''
    i = 0
    j = len(sortablelist)
    while i+1 < j:
        if sortablelist[i] > sortablelist[i+1]:
            return False
        i += 1
    return True
