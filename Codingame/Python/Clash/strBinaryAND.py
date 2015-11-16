import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_1, n_2 = input().split()
for x in range(len(n_1)):
    if (n_1[x] == '1' and n_2[x] == '1'):
        print('1',end='')
    else:
        print('0',end='')
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
