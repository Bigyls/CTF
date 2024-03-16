import string

def banner():
	print('''

.-..-. .-..-. .-..----..----.  .---. 
| ||  `| || | | || {_  | {}  }{_   _}
| || |\  |\ \_/ /| {__ | .-. \  | |  
`-'`-' `-' `---' `----'`-' `-'  `-'  
		''')

result = 7777

def fun08731(nop,hello,n):
	m = ' '
	y = nop[0] + nop[18]+ nop[19] + n + nop[17]
	o = nop[17] + nop[4] + nop[21]+ nop[4] + nop[17] + nop[18] + n
	itx = nop[5] + nop[11] + nop[0] + nop[6]
	u = ':'
	return itx + u + m + o + hello + nop[12] + y

def fun08735(var):
	p = var - 2 
	m = 0
	for x in range(8):
		value = p * 7
		m+=177
		m+=value
	return value

if __name__ == '__main__':
	try:
		banner()
		x = '3'
		it = list(string.ascii_lowercase)
		X = sorted(it, reverse=True)
		noice = '[+] Congratulation you won! \n[*] '
		var = int(input("[+] Please enter the right code : "))
		P = '_'
		p = fun08735(var)
		print(noice + fun08731(it,P,x) + "_1st")

	except:
		x = '3'
		it = list(string.ascii_lowercase)
		X = sorted(it, reverse=True)
		noice = '[+] Congratulation you won! \n[*] '
		var = int(input("[+] Please enter the right code : "))
		P = '_'
		p = fun08735(var)
		print(noice + fun08731(it,P,x) + "_1st")
		print('[!] ERROR')
