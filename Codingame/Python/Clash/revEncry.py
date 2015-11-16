import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

word = input()
for x in word:
    o = ord(x)
    k = 122-o
    print(chr(97+k),end='')
