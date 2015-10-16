import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
matrix = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    matrix.append(line.split())
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while 1:
    x, y, pos = input().split()
    x = int(x)
    y = int(y)
    local = matrix[y][x]
    if (pos == "TOP"):
        if (local in ['1','3','7','9']):
            y += 1
        elif (local in ['4','10']):
            x -= 1
        elif (local in ['5', '11']):
            x += 1
    elif (pos == "LEFT"):
        if (local in ['1','5','8','9','13']):
            y += 1
        elif (local in ['2','6']):
            x += 1
    else:
        if (local in ['1','4','7','8','12']):
            y += 1
        elif (local in ['2','6']):
            x -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(x, y)
