import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binary = ''.join(format(ord(x), 'b').rjust(7,"0") for x in message)
print(binary, file=sys.stderr)

output = ""
count = 0
if (binary[count] == "0"):
    output += "00 "
else:
    output += "0 "
current = binary[count]

while (count < len(binary)):
    if (binary[count] != current):
        if (binary[count] == "0"):
            output += " 00 "
        else:
            output += " 0 "
        current = binary[count]
    output += "0"
    count += 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(output)
