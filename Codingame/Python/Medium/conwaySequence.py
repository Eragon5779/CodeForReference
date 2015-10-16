import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

new = [r]

for x in range(l-1):
    old = list(new)
    new = []
    last = old[0]
    count = 1
    for curr in range(1, len(old)):
        if old[curr] == last:
            count += 1
        else:
            new.append(count)
            new.append(last)
            count = 1
            last = old[curr]
    new.append(count)
    new.append(last)
    print(x, new, old, file=sys.stderr)

print(new, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
out = ""
for x in new:
    out += str(x) + " "

print(out.rstrip())
