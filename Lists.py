def lists():
	my_v = [['johnny','because he acts so good'],['Homer Simpsons','because he is so funny'],['me','because its me']]
	print("My favourite actors are: ")
	for i in my_v:
		for j in i :
			print(j,' ' ,end ='')
		print('.\n')
lists()
