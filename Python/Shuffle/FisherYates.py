from random import randrange

def myShuffle(itemsList):
    """Shuffles items in a list"""
    curr = len(itemsList)
    while curr > 1:
        curr = curr-1
        swap = randrange(curr)
        itemsList[swap], itemsList[curr] = itemsList[curr], itemsList[swap]
    return itemsList
