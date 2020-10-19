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
print('\n')

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
print('\n')
def fun():
	lst = ["Hello", "World", "in", "reallylongword", "a", "frame"] 
	max= 0
	for i  in lst:
		if len(i) > max :
			max = len(i)
	for i in range(max+2):
		print("*",end='')
	print('\n')
	for i  in lst:
		print("*",i,end='')
		for j in range((max-len(i)-1)):
			print(' ',end='')
		print("*")
		print('\n')		
	for i in range(max+2):
                print("*",end='')
fun()
print('\n')

def morcecode(text):
	music_cose = ''
	MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
		
	for i in text:
		if i != ' ':
			music_cose += MORSE_CODE_DICT[i]+ '/'
		else:
			music_cose += '/'
	print(music_cose)

morcecode("GEEKS-FOR-GEEKS")	

print('\n')

def popmorcecode(text):
	text += '/'
	music_cose = ''
	ct = ''
	MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
	for i in text:
		if i != '/':
			j =0
			ct += i
		else:
			j += 1
			if j == 2:
				music_cose += '/'
			else:
				music_cose += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(ct)]
				ct = ''
	print(music_cose)

text = input()
popmorcecode(text)


