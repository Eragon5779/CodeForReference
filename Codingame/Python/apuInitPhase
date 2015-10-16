import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)
message = ""
win = 0
for line in range(len(grid)):
    for char in range(len(grid[line])):
        if (grid[line][char] == "0"):
            message += str(char) + " " + str(line) + " "
            for char2 in range(char+1, len(grid[line])):
                if (grid[line][char2] == "0"):
                    message += str(char2) + " " + str(line) + " "
                    win = 1
                    break
            if (win == 0):
                message += "-1 -1 "
            win = 0
            for line2 in range(line+1, len(grid)):
                if (grid[line2][char] == "0"):
                    message += str(char) + " " + str(line2)
                    win = 1
                    break
            if (win == 0):
                message += "-1 -1"
            win = 0
            print (message)
        message = ""

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# Three coordinates: a node, its right neighbor, its bottom neighbor

