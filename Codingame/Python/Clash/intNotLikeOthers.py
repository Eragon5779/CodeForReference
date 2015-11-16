import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

numbers = [int(x) for x in input().split()]
u = 0
d = 0
for x in numbers:
    if x >= 0:
        u += 1
    else:
        d += 1
if u == 1:
    for x in numbers:
        if x >= 0:
            print(x)
else:
    for x in numbers:
        if x < 0:
            print(x)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


