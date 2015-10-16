import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
a = []
b = []
for i in range(h):
    row = input()
    a.append([row[i:i+l] for i in range(0, len(row), l)])
    b.append("")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for char in t:
    if (char.isalpha()):
        num = ord(char.upper())-65
    else:
        num = -1
    for line in range(h):
        b[line] += a[line][num]

for line in range(h):
    print (b[line])
