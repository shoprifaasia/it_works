def one():
	lst =[]
	print("Enter quit if stooped to added else ")
	x = input("Enter added for pizza: ")
	while( x != 'quit'):
		lst += [x]
		print("Enter quit if stopped to added else ")
		x = input("Enter added for pizza: ")
		
	print("this is your orders for pizza", lst,"\n thanks your pizza in progressing")


def cinema():
	amount =0
	x = input("Enter your age: ")
	while int(x) != 0:
		if int(x) >0 and int(x) < 3:
			print("your ticket is free")
		if int(x) >=3 and int(x) <= 12:
			amount += 10
		else:
			amount += 12
		x = input("Enter your age: ")
	print("check", amount,"dollars")


def whileendtobeg():
	lst = ['yussif','cenime','azbarga','refaa','test']
	x= len(lst)-1
	while x >= 0 :
		print(lst[x])
		x -= 1

def num5to100():
	i = 5
	while( i>=5 and i<=100):
		print(i)
		i += 1


def amountoftickets():
	amount =0
	x = int(input("enter age: "))
	while x > 0:
		if x < 3 :
			print("this is free")
		if x >=3 and  x <=12 :
			amount += 10
		else:
			amount += 12
		x = int(input("enter age"))
	print("you must check ",amount ,"dollars")

def cinemaacceptformovie():
	lstcant = []
	x = int(input("enter age: "))
	while x > 0:
		if x >= 16 and x <= 21 :
			print("can you pyment to see movie restricted")
			id = input("your id: ")
			lst += id
		else:
                        print("can't see movie restricted, please choose another movie")
		x = int(input("enter age"))
	print("this ages accept to see movie restricted ",lst)


def divisibleby7():
	i = 1500
	while i <= 2700:
		if i%7 == 0 and i%5==0:
			print(i)
		i +=1

def numberspaces():
	st= "refaa azbr hi hello world "
	count =0
	i =0
	while i < len(st) :
		if st[i] == ' ':
			count += 1
		i +=1
	print("number of spaces are ",count)
def numberword():
	st= "    refaa azbr hi hello world test    "
	count =0
	i =0
	while i < len(st) :
		if i != 0 :
			if (st[i] == ' ' and i != len(st)-1 and st[i+1] != ' ') or (st[i] != ' ' and i == len(st)-1) :
				count += 1
		i +=1
	print("number of words are ",count)
def isupper():
	st= "    reFaa aZbr hi hEllo wOrld test    "
	countupper =0
	countlower =0
	i =0
	while i < len(st) :
		if st[i].isupper():
			countupper +=1
		else:
			countlower +=1
		i +=1
	print("number of upper latter is ",countupper, "number of lawer latter is ",countlower)


def addtolist():
	i =0
	current_players = ['Mario', 'Luigi', 'Peach']
	new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
	while new_players:
		current_players += [new_players.pop(-1)]
		i +=1
	print(current_players)

def passw():
	pas = input("Enter password: ")
	i =0
	stpass=''
	while i < len(pas):
		stpass += '*'
		i += 1
	print('"',stpass,'"')

def passwsandwich_orders():
	sandwich_orders = ['1sandwich','2sandwich','3sandwich','4sandwich','5sandwich','6sandwich']
	finished_sandwiches = []
	while sandwich_orders:
		print(sandwich_orders.pop(-1))
	sand = input("your order from menu: ")
	while sand != '':
		print("i made your",sand,"sandwich")
		finished_sandwiches.append(sand)
		sand = input("your order from menu : ")
	print("this sandwich is was made: ")
	while finished_sandwiches:
		print(finished_sandwiches.pop(-1))
	

def Encryption(str, num):
	stcyper = ''
	i=0
	while i < len(str):
		x = ord(str[i])
		if str[i].isupper():
			x = (x+num-65)%26
			stcyper +=chr(x+65)	
		else:
			x = (x+num-97)%26
			stcyper += chr(x+97)
		i+=1
	print(stcyper)
Encryption("ATTACKATONCE" ,4)
	

def Decryption(str, num):
        stcyper = ''
        i=0
        while i < len(str):
                x = ord(str[i])
                if str[i].isupper():
                        x = (x-num-65)%26
                        stcyper +=chr(x+65)
                else:
                        x = (x-num-97)%26
                        stcyper += chr(x+97)
                i+=1
        print(stcyper)
Decryption("EXXEGOEXSRGI" ,4)
