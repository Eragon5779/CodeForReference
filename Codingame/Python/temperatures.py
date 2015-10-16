import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
temps = temps.split()
if len(temps) == 0:
    print ("0")
else:
    result = max(temps)
    for x in temps:
        if abs(int(x)) < abs(int(result)):
            result = x
        elif abs(int(x)) == abs(int(result)) and int(x) > 0:
            result = x

    print(result)
