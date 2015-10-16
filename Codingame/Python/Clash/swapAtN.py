import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
word = input()
n %= len(word)

out = word[n:] + word[:n]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(out)
