import unittest
from tdd import solution
class TestSolution(unittest.TestCase):
	"""
	This class holds tests for the solution function
	"""
	
	def test_addition(self):
		"""Tests the addition operator"""
		self.assertTrue(solution(10, 20, "+"), 30)
	
	def test_subtraction(self):
		"""Tests the subtraction operator"""
		self.assertTrue(solution(40, 30, "-"), 10)
	
	def test_multiplication(self):
		"""Tests the multiplication operator"""
		self.assertTrue(solution(10, 10, "*"), 100)
	
	def test_division(self):
		"""Tests the division operator"""
		self.assertTrue(solution(100, 5, "/"), 20)
	
	def test_invalid(self):
		"""Tests if an invalid  operator is passed."""
		self.assertTrue(solution(100, 20, "=*"), "Invalid operation passed.")
	
	def test_modulus(self):
		"""Tests the modulus operator"""
		self.assertTrue(solution(12, 5, "%"), 2)
		

if __name__ == "__main__":
	unittest.main()