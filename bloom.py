from bitarray import bitarray
import mmh3

class Bloom:
	def __init__(self, size, hash_count):
		self.size = size
		self.hash_count = hash_count
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self, string):
		for seed in range(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			self.bit_array[result] = 1

	def lookup(self, string):
		for seed in range(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"


#bf = Bloom(50000, 7)
#words = ["hello", "cat", "dog", "mice", "apple", "microsoft", "google", "Google", "rosewald"]
#for x in words:
#	bf.add(x)

