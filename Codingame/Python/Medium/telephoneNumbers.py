import sys
import math
import functools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
nums = []
for i in range(n):
    telephone = input()
    nums.append(telephone)

size = 0
book = {}

def getFromDict(dataDict, mapList):
    return functools.reduce(lambda d, k: d[k], mapList, dataDict)
    
def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value



for x in nums:
    path = []
    for y in x:
        path.append(y)
        try:
            getFromDict(book, path)
        except:
            setInDict(book, path, {})
            size += 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The number of elements (referencing a number) stored in the structure.
print(size)
