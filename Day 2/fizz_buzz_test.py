import unittest
import fizzbuzz as testcases

class fizz_buzz_tester(unittest.TestCase):
	"""
     The methods below define the testcases for the method fizzbuzz.
     Test the divisibility of the number passed by 3,5,both 3 and 5.
	"""
    
	def test_fizz_1(self):
        self.assertEqual(testcases.fizz_buzz(6), "Fizz")
    
    def test_fizz_2(self):
        self.assertEqual(testcases.fizz_buzz(9), 'Fizz')
    
    def test_buzz_1(self):
        self.assertEqual(test_cases.fizz_buzz(20), 'Buzz')
    
    def test_buzz_2(self):
        self.assertEqual(test_cases.fizz_buzz(100), 'Buzz')

    def test_fizz_buzz_1(self):
        self.assertEqual(testcases.fizz_buzz(45), 'FizzBuzz')
    
    def test_fizz_buzz_2(self):
        self.assertEqual(testcases.fizz_buzz(75), 'FizzBuzz')
        
    def test_indivisible_1(self):
        self.assertEqual(testcases.fizz_buzz(98), 98)
        
    def test_indivisible_2(self):
self.assertEqual(testcases.fizz_buzz(7), 7)