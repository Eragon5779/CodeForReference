import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
d = {}
exited = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if (n1 in d):
        d[n1].append(n2)
        exited[n1].append(n2)
    else:
        d[n1] = [n2]
        exited[n1] = [n2]
    if (n2 in d):
        d[n2].append(n1)
        exited[n2].append(n1)
    else:
        d[n2] = [n1]
        exited[n2] = [n1]
exits = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)
# game loop
out = 0
delete = []
while 1:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    for x in exits:
        if (si in d[x]):
            y = si
            print(x,si)
            d[x].remove(y)
            d[y].remove(x)
            out = 1
    if (out == 0):
        for x in exits:
            for y in d[x]:
                if (si in d[y]):
                    z = si
                    print(z,y)
                    d[z].remove(y)
                    d[y].remove(z)
                    out = 1
                    break
            if (out == 1):
                break
    if (out == 0):
        for x in exits:
            for y in d[x]:
                for z in d[x]:
                    if (y in d[z]):
                        print(z,y)
                        d[z].remove(y)
                        d[y].remove(z)
                        out = 1
                        break
                if (out == 1):
                    break
            if (out == 1):
                break
    if (out == 0):
        for x in exits:
            print(x,d[x][0])
            d[d[x][0]].remove(x)
            d[x].remove(d[x][0])
            out = 1
            break
    out = 0
    for x in d.keys():
        if (d[x] == []):
            delete.append(x)
    for x in delete:
        del d[x]
        if x in exits:
            exits.remove(x)
    delete = []
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
