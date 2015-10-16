import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
one = []
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    one.append(cardp_1[:-1])
m = int(input())  # the number of cards for player 2
two = []
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    two.append(cardp_2[:-1])
count = 0
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
bufferOne = []
bufferTwo = []
pat = 0
while (len(two) > 0 and len(one) > 0):
    print(one, file=sys.stderr)
    print(two, file=sys.stderr)
    if (cards[one[0]] > cards[two[0]]):
        for x in bufferOne:
            one.append(x)
        one.append(one.pop(0))
        for x in bufferTwo:
            one.append(x)
        one.append(two.pop(0))
        bufferOne = []
        bufferTwo = []
        print("one", file=sys.stderr)
    elif (cards[one[0]] < cards[two[0]]):
        for x in bufferOne:
            two.append(x)
        two.append(one.pop(0))
        for x in bufferTwo:
            two.append(x)
        two.append(two.pop(0))
        bufferOne = []
        bufferTwo = []
        print("two", file=sys.stderr)
    else:
        if (len(one) < 4 or len(two) < 4):
            pat = 1
        for x in range(4):
            if one:
                bufferOne.append(one.pop(0))
            if two:
                bufferTwo.append(two.pop(0))
        count -= 1
    count += 1
    print(count, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if (pat == 1):
    print("PAT")
elif(len(two) > 0):
    print("2", count)
else:
    print("1", count)
