def helper(m):
    if m < 10:
        return (m, 0)
    count = 1
    k = m//10
    k -= 2 * (m % 10)
    if k > 100:
        a = helper(k)
        count += a[1]
        k = a[0]
    return (k, count)
        

def seven(m):
    return helper(m)
    # your code
