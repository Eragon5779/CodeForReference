import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, h = [int(i) for i in input().split()]
g = []
for i in range(h):
    numeral = input()
    g.append([ numeral[start:start+l] for start in range(0, len(numeral), l) ])
s1 = int(input())
first = []
firstNum = 0
winner = 1
for i in range(s1):
    num_1line = input()
    first.append(num_1line)
for line in range(0, s1, h):
    for num in range(len(g[0])):
        for x in range(h):
            if (g[x][num] != first[x+line]):
                winner = 0
        if (winner == 1):
            firstNum += int(num * 20**((s1/h)-((line/h)+1)))
            break
        winner = 1
s2 = int(input())
second = []
secondNum = 0
for i in range(s2):
    num_2line = input()
    second.append(num_2line)
for line in range(0, s2, h):
    for num in range(len(g[0])):
        for x in range(h):
            if (g[x][num] != second[x+line]):
                winner = 0
        if (winner == 1):
            secondNum += int(num * 20**((s2/h)-((line/h)+1)))
            break
        winner = 1
operation = input()
ops = {'+': (lambda x,y: x+y), '-': (lambda x,y: x-y), '*': (lambda x,y: x*y), '/': (lambda x,y: x/y)}

final = ops[operation](firstNum, secondNum)
power = 1
copy = final
while copy > 20:
    power += 1
    copy = copy/20
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(final, firstNum, secondNum, file=sys.stderr)
for x in range(power, 0, -1):
    for i in range(h):
        print (g[i][int((final/(20**(x-1)))%20)])
