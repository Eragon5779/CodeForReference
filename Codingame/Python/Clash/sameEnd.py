import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s1, s2 = input().split()

if str(s1[-4:]) == str(s2[-4:]):
    print(1)
else:
    print(0)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
