import unittest
import data_type as testcases

class data_type_tester(unittest.TestCase):
	"""
    This is a class that tests the various types provided by the user to the method
    and returns the appropriate message.
	"""

 def test_none_type(self):
    self.assertEqual(testcases.data_type(None),'no value' )

  def test_list_type(self):
    self.assertEqual(testcases.data_type([1, 2, 3], 3))

  def test_small_list_len(self):
    self.assertEqual(testcases.data_type([1]), None)

  def test_bool_type(self):
    self.assertEqual(testcases.data_type(False), False)

  def test_small_int_type(self):
    self.assertEqual(testcases.data_type(30), 'less than 100')

  def test_large_int_type(self):
    self.assertEqual(testcases.data_type(300), 'more than 100')
  
  def test_str_type(self):
    self.assertEqual(testcases.data_type('angela'), 6)