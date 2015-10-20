def pattern(n):
    if n < 1:
        return ""
    out = ""
    x = range(1, n+1)
    x.reverse()
    length = len(x)
    for i in xrange(length):
        out += ''.join(str(y) for y in x)
        out += '\n'
        del x[-1]
    return out[:-1]
    # Happy Coding ^_^
