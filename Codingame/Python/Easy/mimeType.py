import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    d[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    fname = fname.split(".")
    if (fname[-1].lower() in d and len(fname) > 1):
        print(d[fname[-1].lower()])
    else:
        print("UNKNOWN")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
