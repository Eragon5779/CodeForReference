import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
horses = []
n = int(input())
for i in range(n):
    pi = int(input())
    horses.append(int(pi))
horses.sort()
min = 10000000
for x in range(n-1):
    if horses[x+1] - horses[x] < min:
        min = horses[x+1] - horses[x]
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min)
