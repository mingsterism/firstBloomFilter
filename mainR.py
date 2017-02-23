from src import bloom
import random

def readfile():
	bf = bloom.Bloom(50000000, 10)
	with open('mfundslist.txt', 'r') as funds:
		for x in funds.readlines():
			bf.add(x.split("|")[0])
	return bf

def bloomFundsTest(bloomfilter):
	probably = 0
	total = 0
	with open('mfundslist.txt', 'r') as funds:
		for x in funds.readlines():
			total += 1
			if bloomfilter.lookup(x.split("|")[0]) == "Probably":
				probably += 1
	return {"ratio hits": probably / total, "probably":probably, "total":total}

def bloomRandomNumTest(bloomfilter, rounds):	
	total = 0
	wrongs = 0
	for x in range(rounds):
		total += 1
		num = str(random.randint(0, 10000))
		if bloomfilter.lookup(num) == "Probably":
			wrongs += 1
	return {"total":total, "wrongs":wrongs, "ratio wrongs": wrongs/ total}

if __name__ == "__main__":
	print(bloomFundsTest(readfile()))
	print(bloomRandomNumTest(readfile(), 10000))
