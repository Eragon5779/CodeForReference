import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
a = {}
b = {"LEFT": -1, "RIGHT": 1}
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    a[elevator_floor] = elevator_pos

block = width/2
one = 0
# game loop
while 1:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    print(exit_floor, exit_pos, clone_pos, clone_floor, direction, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # action: WAIT or BLOCK
    if (clone_floor == exit_floor):
        if (clone_pos < exit_pos):
            if (direction == "RIGHT"):
                print("WAIT")
            else:
                print("BLOCK")
        else:
            if (direction == "RIGHT"):
                print("BLOCK")
            else:
                print("WAIT")
    elif (clone_floor < 0):
        print("WAIT")
    elif ((clone_pos - a[clone_floor])*b[direction] <= 0):
        print("WAIT")
    else:
        if (one >= 1):
            print("BLOCK")
            one = 0
        else:
            print("WAIT")
            one += 1
    #if (clone_pos == 0 or clone_pos == width - 1):
    #    print("BLOCK")
    #else:
    #    print("WAIT")
