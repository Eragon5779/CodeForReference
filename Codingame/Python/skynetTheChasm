import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

print (road, file=sys.stderr)
print (gap, file=sys.stderr)

neededSpeed = gap + 1
output = "SPEED"
# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.
    print (coord_x, file=sys.stderr)
    if output == "JUMP":
        output = "SLOW"
    elif coord_x < road + 1:
        print (coord_x, file=sys.stderr)
        if speed < neededSpeed:
            output = "SPEED"
        elif speed > neededSpeed:
            output = "SLOW"
        else:
            output = "WAIT"
        if road + gap <= coord_x + speed:
            output = "JUMP"
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    print(output)
