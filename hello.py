def x():
	for i in range(6):
     		for j in range(i+1):
             		print("X", end = '')
     		print('\n')
	for i in range(6):
		for j  in range(6-i-1):
            		 print("X", end = '')
		print('\n')
	x = input("what's your name: ")	
	if len(x) > 0:
		print(x ,"welcome")
	else:
		print("don't have name ia baghetl!!")

def y():
	st = "your name is longest"
	x = input("Enter your name: ")
	y = input("Enter second name: ")
	if len(x) > len(y):
		print(x,st)
	else:
		print(y,st)

def yy():
	bd = input("enter your birthday - DD/MM/YYYY: ")
	st = bd[6:]
	print("your old this year is ",2020-int(st) ,"years old") 


def exercisehard():
	bd = input("enter your birthday - DD/MM/YYYY: ")
	str = bd[6:]
	print(str)
	year = 2020 -int(str)
	month = bd[3:5]
	print(month)
	moncurrent =10 -int(month)
	day = bd[0:2]
	print(day)
	d = 18 - int(day)
	print("your age is : ",year, "years, ",moncurrent,"month and",d,"days years old")

def exerciseharde():
	current_players = ['Mario', 'Luigi', 'Peach']
	new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
	for i  in new_players:
		current_players += [i]
	print(current_players)


def star():
	for i in range(5):
		for j in range(i+1):
			print("*",end = '')
		print('\n')

def starup():
	for i in range(5):
                for j in range(i+1):
                        print("*",end = '')
                print('\n')
	for i in range(5):
		for j  in range(5-i):
			print("*",end = '')
		print('\n')
		if (i < 4):
			for k  in range(i+1):
				print(" ",end = '')

def staruptringle():
	for i in range(3):
		if (i < 3):
                       	for k  in range(3-i):
                               	print(" ",end = '')
		x = i*2+1
		for j in range(x):
			print("*",end = '')
		print('\n')

def listwithoutsplit():
	lst= []
	str = ''
	st = "my name is refaa azbarga"
	for i in st:
		if i != ' ':
			str += i
		else:
			lst += [str]
			str = ''
	print(lst)

def longwordinlist():
	ls= ['refaa','azbarga','yussif','hello']
	max = ls[0]	
	for i in ls:
		if len(max) < len(i):
			max = i
	print("long word in list - ",max)
longwordinlist()
		
