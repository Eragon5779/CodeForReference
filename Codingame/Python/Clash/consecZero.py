import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
c = 0
t = 0
for x in n:
    if x == '0':
        t += 1
    else:
        if t > c:
            c = t
        t = 0
if t > c:
    c = t
print(c)
