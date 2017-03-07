import unittest
from tdd import solution
class TestSolution(unittest.TestCase):
	
	def test_addition(self):
		self.assertTrue(solution(10, 20, "+"), 30)
	
	def test_subtraction(self):
		self.assertTrue(solution(40, 30, "-"), 10)
	
	def test_multiplication(self):
		self.assertTrue(solution(10, 10, "*"), 100)
	
	def test_division(self):
		self.assertTrue(solution(100, 5, "/"), 20)
	
	def test_invalid(self):
		self.assertTrue(solution(100, 20, "=="), "Invalid operation passed.")
	
	def test_modulus(self):
		self.assertTrue(solution(12, 5, "%"), 2)
		

if __name__ == "__main__":
	unittest.main()