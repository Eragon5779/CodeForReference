l = []
for x in range(int(input())):
  l.append(int(input()))
l.sort()
print(' '.join(str(x) for x in l[::-1]))
