import sys

def get_gcd(first, second):
	if first < second:
		small = first
		large = second
	else:
		small = second
		large = first
	while (large % small) != 0:
		large = large % small
		# swap small and large
		small = small + large
		large = small - large
		small = small - large
#	print("GCD of %d and %d is %d" % (first, second, small))
	return small

def get_int_list(strs):
	L = []
	for str in strs:
		L.append(int(str))
	return L

def is_prime_missing(primes):
	prime_missing = False
	for prime in primes:
		if prime == 0:
			prime_missing = True
			break
	return prime_missing

def calculate_missing_primes(products, primes):
	# assume list doesn't start with a misisng prime
	count = len(primes)
	for i in range(count):
		if (primes[i] == 0):
			if i > 0 and (primes[i - 1] > 0):
				primes[i] = int(products[i - 1] / primes[i - 1])
			else:
				index = i + 1
				while(primes[index] == 0):
					index += 1
				while(index > i):
					primes[index - 1] = int(products[index - 1] / primes[index])
					index -= 1
	return primes		
			

def get_primed_plaintext(ciphertext):
	products = get_int_list(ciphertext.split())
	primed_plaintext = [0]
	no_products = len(products)
	for i in range(no_products - 1):
		primed_plaintext.append(0 if (products[i] == products[i+1]) else get_gcd(products[i], products[i+1]))
	# calculate first and last elements as we currently only have [1:n] elements
	primed_plaintext[0] = int(products[0] / primed_plaintext[1]) if primed_plaintext[1] > 0 else 0
	primed_plaintext.append(int(products[no_products - 1] / primed_plaintext[no_products - 1]) if primed_plaintext[no_products - 1] > 0 else 0)
	if is_prime_missing(primed_plaintext):
		primed_plaintext = calculate_missing_primes(products, primed_plaintext)
	return primed_plaintext

def remove_duplicates(input):
	L = []
	for num in input:
		if len(L) == 26:
			break
		if num not in L:
			L.append(num)
	return L

def get_char_from_sorted_ptext(ptext, prime):
	for char in ptext:
		if char[0] == prime:
			return char[1]

def printplaintext(plaintext):
	for char in plaintext:
		print(char, end = '')
	print()

def main():
	cases = int(sys.stdin.readline().rstrip())
	iteration = 1
	while iteration <= cases:
		input_count = sys.stdin.readline().split()[1]
		ciphertext = sys.stdin.readline().rstrip()
		primed_ptext = get_primed_plaintext(ciphertext)
		sorted_ptext = remove_duplicates(primed_ptext)
		sorted_ptext.sort()
		# print(primed_ptext)
		# print(sorted_ptext)
		for i in range(len(sorted_ptext)):
			sorted_ptext[i] = [sorted_ptext[i], chr(ord('A') + i)]
		
		# print(sorted_ptext)
		plaintext = []
		for i in range(len(primed_ptext)):
			plaintext.append(get_char_from_sorted_ptext(sorted_ptext, primed_ptext[i]))
		print("Case #%d: " % iteration, end='')
		printplaintext(plaintext)
		iteration += 1

def testmain():
	num1 = 2**30 - 41
	num2 = 2**36 - 5
	num3 = 2**70 - 35
	print("%d times %d = %d" % (num1, num3, num1 * num3))
	print("%d times %d = %d" % (num2, num3, num2 * num3))
	print("GCD is %d" % get_gcd(num1 * num3, num2 * num3))

if __name__ == "__main__":
	main()