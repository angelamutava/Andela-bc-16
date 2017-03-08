from person import Person, StaffMember, Lecturer, Student

import unittest

class PersonTest(unittest.TestCase):
    """An instance of class person"""

    def test_class_person(self):
        angie = Person("Angela", "Mutava")
        self.assertIsInstance(angie, Person, msg='The instance should be of class Person')

    def test_child_class_student(self):
        """Testing an instance of class Student"""
        angie = Student("parallel student", "Angela", "Mutava")
        self.assertIsInstance(angie, Student, msg='The instance should be of class Student')

    def test_child_class_staff_member(self):
        """Testing an instance of class Student"""
        angie = StaffMember("permanent", "Angela", "Mutava")
        self.assertIsInstance(angie, StaffMember, msg='The instance should be of class StaffMember')

    def test_child_class_lecturer(self):
        """Testing an instance of class Student"""
        angie = Lecturer("permanent", "Angela", "Mutava")
        self.assertIsInstance(angie, Lecturer, msg='The instance should be of class Lecturer')

    def test_inheritance(self):
        """testing whether the object for lecturer is able to call the method for test employment """
        angie = Lecturer("permanent", "Angela", "Mutava")
        angie.is_permanent()
self.assertEqual(angie.is_permanent(), True)