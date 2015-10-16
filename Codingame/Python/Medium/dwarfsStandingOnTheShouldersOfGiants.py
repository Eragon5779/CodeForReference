import sys
import math

def count(x, d):
    if len(d[x]) > 0:
        current = 1
        for y in d[x]:
            tmp = count(y, d)
            if tmp > current:
                current = tmp
        return current + 1
    return 1

def main():
    n = int(input())
    d = {}
    root = []
    for i in range(n):
        x, y = map(int,input().split())
        if x not in d:
            d[x] = []
        if y not in d:
            d[y] = []
        d[x].append(y)
        root.append(x)

    for x in d:
        for y in d[x]:
            if y in root:
                root.remove(y)
                
    longest = 0
    print(d, file=sys.stderr)
    for x in root:
        print(x, file=sys.stderr)
        current = count(x, d)
        if current > longest:
            longest = current
    
    print(longest)

main()
