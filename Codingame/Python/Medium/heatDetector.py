import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
lw = 0
rw = w
bh = h
th = 0
# game loop
while 1:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if ("U" in bomb_dir):
        bh = y
        y = int((y + th)/2)
    elif ("D" in bomb_dir):
        th = y
        y = int((y + bh)/2)
    if ("R" in bomb_dir):
        lw = x
        x = int((x + rw)/2)
    elif ("L" in bomb_dir):
        rw = x
        x = int((x + lw)/2)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.
    print(x, y)
