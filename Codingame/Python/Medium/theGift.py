import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
g = []
for i in range(n):
    b = int(input())
    g.append(b)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
g.sort()
if sum(g) < c:
    print("IMPOSSIBLE")
else:
    y = c
    z = n
    avg = y/z
    out = []
    for x in range(len(g)):
        if g[x] < avg:
            out.append(g[x])
            y -= g[x]
            z -= 1
            avg = y/z
    extra = y%z
    avg = int(y/z)
    for x in range(z):
        if x < extra:
            out.append(avg+1)
        else:
            out.append(avg)
        
    out.sort()
    for x in out:
        print(x)
