import math
a,b=map(float,input().split())
c,d=map(float,input().split())
x=math.ceil(a/d);y=math.ceil(c/b)
print(('1 '+str(y),'2 '+str(x))[x<y])
