def grader(score):
	if score < 0.6 or score > 1.0:
		return 'F'
	elif score >= 0.9:
		return 'A'
	elif score >= 0.8:
		return 'B'
	elif score >= 0.7:
		return 'C'
	else:
		return 'D'
