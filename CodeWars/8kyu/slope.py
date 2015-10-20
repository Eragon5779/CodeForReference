def find_slope(points):
    x = points[0] - points[2]
    y = points[1] - points[3]
    if x == 0:
        return 'undefined'
    else:
        return str(y/x)
