import re

out = 0
n = int(input())
for x in n:
  test = input()
  result = re.findall("|[0-9]+|", test)
  out += len(result)

print(out)
