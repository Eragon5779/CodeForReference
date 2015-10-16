import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = {}

for i in range(n):
    x, y = [int(j) for j in input().split()]
    try:
        c[x].append(y)
    except:
        c[x] = [y]

minx = min(list(c.keys()))
maxx = max(list(c.keys()))

ys = []

for x in c:
    for y in c[x]:
        ys.append(y)

miny = min(ys)
maxy = max(ys)

main = 0

avg = 0

for x in c:
    for y in c[x]:
        avg += y

avg = round(avg/n)

            
d = {}

for x in c:
    for y in c[x]:
        try:
            d[y] += 1
        except:
            d[y] = 1

shift = 1

while (shift != 0 and avg != max(d, key=d.get)):
    shift = 0
    for x in c:
        for y in c[x]:
            if y > avg:
                shift += 1
            elif y < avg:
                shift -= 1
    if shift > 0:
        miny = avg
        avg = round((avg + maxy)/2)
    elif shift < 0:
        maxy = avg
        avg = round((avg + miny)/2)

main = avg

lines = maxx - minx

print(main, avg, c, lines, file=sys.stderr)

for x in c:
    for y in c[x]:
        lines += math.fabs(y - main)

three = lines


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(int(three))
