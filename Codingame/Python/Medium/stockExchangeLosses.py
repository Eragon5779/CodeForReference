import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = input()

s = [int(x) for x in s.split()]
order = list(set(s))
order.sort(reverse=True)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
m = 0

for x in order:
    if (-x > m):
        break
    loc = s.index(x)
    if (min(s[loc:]) - x < m):
        m = min(s[loc:]) - x

print(m)
