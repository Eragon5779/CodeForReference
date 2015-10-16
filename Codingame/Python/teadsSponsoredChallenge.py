import sys
import math


class result:
    length = 0
    last = 0

class node:
    neighbs = []
    n = 0
    
    def __init__(self, n):
        self.n = n
        self.neighbs = []
    
    def add(self, n):
        self.neighbs.append(n)

def readinfo():
    graph = []
    
    n = int(input())
    for i in range(n):
        # xi: the ID of a person which is adjacent to yi
        # yi: the ID of a person which is adjacent to xi
        xi, yi = map(int,input().split())
        while (len(graph)-1 < max(xi, yi)):
            graph.append(node(len(graph)))
        graph[xi].add(graph[yi])
        graph[yi].add(graph[xi])
    return graph

def bfs(start, graph):
    res = result()
    
    depth = [-1 for x in range(len(graph))]
    depth[start.n] = 0
    
    stack = []
    stack.append(start)
    
    while (len(stack) > 0):
        father = stack.pop()
        sons = father.neighbs
        for son in sons:
            if (depth[son.n] == -1):
                depth[son.n] = depth[father.n]+1
                if (depth[son.n] > res.length):
                    res.length = depth[son.n]
                    res.last = son
                stack.append(son)
    return res

def main():
    graph = readinfo()
    r = bfs(graph[0], graph)
    r = bfs(r.last, graph)
    print(int((r.length+1)/2))
    
main()
