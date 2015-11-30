s=list(input())
k=['O','L','Z','E','A','S','G','T','B','Q']
for x in range(len(s)):
    t=s[x].upper()
    if t in k:s[x]=str(k.index(t))
print(''.join(s))
