import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = input()
o = ''
k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for x in c:
    if x == '#':
        o += "#"
    else:
        t = k.index(x)
        o += k[15-t]
            

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(o)
