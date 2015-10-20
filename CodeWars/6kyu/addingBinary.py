def btoi(a):
	x = 0
	for i in xrange(len(a)):
		if a[i] == '1':
			x += 2 ** i
	return x

def itob(a):
	if a == 0:
		return '0'
	x = ''
	while a > 0:
		if a % 2 == 1:
			x += '1'
		else:
			x += '0'
		a /= 2
	return x[::-1]

def add(a,b):
	x = btoi(a[::-1])
	y = btoi(b[::-1])
	z = x + y
	return itob(z)
