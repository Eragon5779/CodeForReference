import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c = [int(i) for i in input().split()]
matrix = []
for i in range(l):
    row = input()
    matrix.append(list(row))

h = "SOUTH"
turn = ["SOUTH", "EAST", "NORTH", "WEST"]
xd = {"WEST": -1, "EAST": 1, "SOUTH": 0, "NORTH": 0}
yd = {"SOUTH": 1, "NORTH": -1, "WEST": 0, "EAST": 0}
turns = {"S": "SOUTH", "N": "NORTH", "W": "WEST", "E": "EAST"}
x = 0
y = 0
mode = 0
loop = 0
common = 0

for line in range(l):
    for spot in range(c):
        if matrix[line][spot] == "@":
            y = line
            x = spot

tx = x
ty = y

t =[]
for line in range(len(matrix)):
    for char in range(len(matrix[line])):
        if matrix[line][char] == "T":
            t.append([line,char])

out = []
loops = []

print(matrix, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
while 1:
    print(ty, tx, y, x, mode, file=sys.stderr)
    tx += xd[h]
    ty += yd[h]
    loop = 0
    if (matrix[y][x] == "B"):
        if mode == 1:
            mode = 0
        else:
            mode = 1
    if (matrix[ty][tx] == "X" and mode == 1):
        matrix[ty][tx] = " "
    elif (matrix[ty][tx] == "I"):
        turn.reverse()
    while (matrix[ty][tx] == "#" or (matrix[ty][tx] == "X" and mode == 0)):
        h = turn[loop]
        tx = x + xd[h]
        ty = y + yd[h]
        loop += 1
    x = tx
    y = ty
    out.append(h)
    if (matrix[ty][tx] == "$"):
        break
    elif (matrix[ty][tx] in ["N","S","W","E"]):
        h = turns[matrix[ty][tx]]
    elif (matrix[ty][tx] == "T"):
        for pad in t:
            if (pad[0] != ty or pad[1] != tx):
                y = pad[0]
                x = pad[1]
                ty = y
                tx = x
                break
    if ([x,y,h,turn,mode,matrix] not in loops):
        loops.append([x,y,h,turn,mode,matrix])
        common = 0
    else:
        common += 1
    if (common > c*l):
        out = ["LOOP"]
        break

for x in out:
    print(x)
