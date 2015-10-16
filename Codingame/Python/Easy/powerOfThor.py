import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
direction = ""
thorX = initial_tx
thorY = initial_ty
# game loop
while 1:
    remaining_turns = int(input())
    if (thorY < light_y):
        direction += "S"
        thorY += 1
    elif (thorY > light_y):
        direction += "N"
        thorY -= 1
    if (thorX < light_x):
        direction += "E"
        thorX += 1
    elif (thorX > light_x):
        direction += "W"
        thorX -= 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
    direction = ""
