import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()
s = 0
for x in n:
    if int(x) % 2 == 0:
        s += int(x)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(s)
