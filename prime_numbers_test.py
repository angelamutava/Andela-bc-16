import unittest
from prime_numbers import prime_generator

class PrimeGenerator(unittest.TestCase):
	"""
	Defining tests for prime generators.
	"""
	def test_negative_numbers(self):
		"""Tests for negative numbers.
		"""
		self.assertEqual(prime_generator(-5), "Negative numbers not allowed.")

	def test_string(self):
	   """
	   Tests whether the parameter passed to the method is a string.
	   """
	   self.assertEqual(prime_generator("str"), "Only integers allowed.")

	def test_list(self):
	   """
	   Tests whether the parameter passed is a list
	   """ 
	   self.assertEqual(prime_generator([]), "Only integers allowed.") 

	def test_zero(self):
	  """
	  Tests whether zero is prime. 
	  """
	  self.assertEqual(prime_generator(0), [])

	def test_prime_50(self):
	  """
	  Tests the prime numbers genarated within the range 50
	  """
	  self.assertEqual(prime_generator(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

	def test_prime_100(self):
	  """
	  Tests the prime numbers generated within the range 100
	  """
	  self.assertEqual(prime_generator(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) 

	def test_empty_parameters(self):
	  """
	  Tests whether the function has empty parameters
	  """
	  self.assertRaises(prime_generator(), "No parameter has been provided")

	def test_prime_one(self):
	  """
	  Tests whether one is prime.
	  """
	  self.assertEqual(prime_generator(1), [])
    