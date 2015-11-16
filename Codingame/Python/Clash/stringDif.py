a,b=input().split()
o=0
for x in range(len(a)):o+=(1,0)[a[x]==b[x]]
print(o)
