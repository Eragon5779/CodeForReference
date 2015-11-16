w,h=map(int,input().split())
l=[input() for i in range(h)]
o=0
for x in range(1,w-1):
 for y in range(1,h-1):o+=(0,1)[l[y][x-1:x+2]+l[y-1][x]+l[y+1][x]=="X"*5]
print(o)
