def count_arara(n):
    odd = n % 2
    even = n//2
    out = ""
    for x in xrange(even):
        out += "adak "
    if odd == 1:
        out += "anane"
    return out.strip()
