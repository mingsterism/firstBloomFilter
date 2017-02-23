with open('mfundslist.txt', 'r') as funds:

	for x in funds.readlines():
		print(x.split("|")[0])
