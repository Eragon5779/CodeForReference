from re import sub
print(sub(r'(.)\1*',lambda m:str(len(m.group(0)))+m.group(1),input()))
