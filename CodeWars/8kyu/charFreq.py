def char_freq(message):
	d = {}
	for x in message:
		try:
			d[x] += 1
		except:
			d[x] = 1
	return d
