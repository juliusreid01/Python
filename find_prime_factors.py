def fact(n):
	""" Returns n! for all positive n : O(2^n) """
	# negative numbers are not supported
	if n < 0: return None 
	# 0
	if n == 0: return 1
	# less than 3 requires no multiplication
	if n == 1 or n == 2: return 2
	# otherwise solve recursively
	return n * fact(n-1)
	
def is_prime(n):
	""" Returns true if a number is a prime number using ((n-1)!+1) % n == 0 (Wilson's Theorem) """
	# corner case
	if n <= 0: return 0
	# first primes 1, 2, 3
	if n > 0 and n < 4: return 1
	# others
	return (fact(n-1) + 1) % n == 0

def next_prime(n):
	""" Returns the next prime number after the given number """
	if n < 0: return 1
	if n < 3: return n + 1		
	# brute force method TODO. Can we do this faster without brute force???
	while 1:
		n = n + 1
		if is_prime(n): return n
		
def prime_factors(n):
	""" Returns a list of prime factors """
	# corner cases
	if n == 0: return list()
	# prime numbers
	if is_prime(n): return [n]
	# create a new list
	pf = list()
	# iterate from 2 to n/2
	i = 2
	while i <= n:
		# found a prime factor 
		if n % i == 0: 
			n = n / i
			pf.append(i)
		else:
			i = next_prime(i)
			# can use i = i + 1 bc 4 = 2 * 2, 6 = 2 * 3, 8 = 2 * 2 * 2 ...
			
	return pf