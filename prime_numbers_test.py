import unittest
from prime_numbers import prime_generator

class PrimeGenerator(unittest.TestCase):
	"""
	Defining tests for prime generators.
	"""
	def test_negative_numbers(self):
		"""Tests for negative numbers.
		"""
		self.assertTrue(prime_generator(-5), "Negative numbers not allowed.")

	def test_15(self):
	  """
	  Tests whether zero is prime. 
	  """
	  self.assertTrue(prime_generator(15), [2, 3, 5, 7, 11, 13])

	def test_prime_10(self):
	  """
	  Tests the prime numbers genarated within the range 50
	  """
	  self.assertTrue(prime_generator(10), [2, 3, 5, 7])

	def test_prime_2(self):
	  """
	  Tests the prime numbers generated within the range 100
	  """
	  self.assertTrue(prime_generator(2), [2]) 


	def test_prime_12(self):
	  """
	  Tests whether one is prime.
	  """
	  self.assertTrue(prime_generator(12), [2, 3, 5, 7, 11])


if __name__ == "__main__":
	unittest.main()