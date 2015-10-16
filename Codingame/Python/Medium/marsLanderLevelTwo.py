import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append([land_x,land_y])
    
minx = 0
maxx = 0
last = 0

for x in range(1, len(surface)):
    if surface[x][1] == surface[last][1]:
        minx = last
        maxx = x
    last = x

ly = surface[minx][1]
minx = surface[minx][0]
maxx = surface[maxx][0]

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if h_speed < -60 or h_speed > 60:
        d = (-45,45)[h_speed > 60]
        p = 4
    elif x < maxx and x > minx:
        if h_speed < -20:
            d = -60
            p = 4
        elif h_speed > 20:
            d = 60
            p = 4
        else:
            if maxx - x < 200 and h_speed > 0:
                d = 15
            elif minx - x > -200 and h_speed < 0:
                d = -15
            else:
                d = 0
            p = (3,4)[math.sqrt(v_speed**2+((y-ly)*2*(4-3.711))) < -38]
    else:
        d = (30,-30)[x < minx]
        p = 4
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(d,"4")
