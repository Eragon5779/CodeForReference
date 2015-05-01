def cyclesort( aList ):
    writes = 0
    for cs in range( len( aList ) - 1 ):
      seeker = aList[cs]
      pos = cs
      for i in range( cs + 1, len( aList ) ):
        if aList[i] < seeker:
          pos += 1
      if pos == cs:
        continue
      while seeker == aList[pos]:
        pos += 1
      seeker = set_value( aList, seeker, pos )
      writes += 1
      while pos != cs:
        pos = cs
        for i in range( cs + 1, len( aList ) ):
          if aList[i] < seeker:
            pos += 1
        while seeker == aList[pos]:
          pos += 1
        seeker = set_value( aList, seeker, pos )
        writes += 1
    return writes
 
 
def set_value( aList, data, ndx ):
    try:
      return aList[ndx]
    finally:
      aList[ndx] = data
