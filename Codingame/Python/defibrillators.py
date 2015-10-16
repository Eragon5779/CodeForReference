import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lon = float(lon.replace(",", "."))
lat = input()
lat = float(lat.replace(",", "."))
n = int(input())
closest = 0
shortest = 500000
for i in range(n):
    defib = input()
    defib = defib.replace(",", ".")
    defib = defib.split(';')
    x = (float(defib[4]) - lon) * math.cos((float(defib[5]) + lat)/2)
    y = (float(defib[5]) - lat)
    dist = math.sqrt(x**2 + y**2) * 6371
    if dist < shortest:
        shortest = dist
        closest = defib[1]



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(closest)
