def dic():
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}
	for key,value in d2.items():
		if key not in d1.keys():
			d1[key] = value
		else:
			d1[key] = d1[key]+value
	print(d1)

dic()
