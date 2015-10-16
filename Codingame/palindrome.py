import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in range(n):
    w = input()
    a.append(w)
    
for x in a:
    if str(x) == str(x)[::-1]:
        print("true")
    else:
        print("false")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
