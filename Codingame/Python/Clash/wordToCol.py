s=input().replace(" ","")
c=int(input())
print(*[s[i:i+c] for i in range(0,len(s),c)],sep='\n')
