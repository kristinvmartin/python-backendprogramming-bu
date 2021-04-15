"""
Kristin Martin
CS 521
March 10, 2019
Term Project Submission: Unit Testing

This script contains a few unit tests that can be implemented with the program.
It is by no means exhaustive unit testing, just a sampling.

Note: BeginSunday.sample_setup() was used to test the children directory, however
any instance of a dictionary containing children keys and objects could be substituted.

Note: Exception handling was largely handled through try blocks wrapped in while loops,
so no unit testing was performed on those sections of code.

"""
import unittest
import BeginSunday
from SundaySchoolClass import SundaySchoolClass

class TestFile1(unittest.TestCase):
    
    def test_file_categories(self):
        """tests to make sure teacher assignments are from established categories"""
        teacher_assignments = BeginSunday.setup_teacher_assignments('Teachers.txt')
        categories = SundaySchoolClass.categories
        for assignment in range(len(teacher_assignments)):
            self.assertIn(list(teacher_assignments.keys())[assignment],categories)
        print()
        print("Test1 file categories success.")

class TestNamingConvention(unittest.TestCase):
    
    def test_naming_convention(self):
        """tests the naming convention is consistent across all Child objects in
        the children dictionary"""
        children = BeginSunday.sample_setup()
        children_list = list(children.keys()) #list of keys
        for i in range(len(children)):
            self.assertEqual(children_list[i],
                             children[children_list[i]].get_first_name() + 
                             children[children_list[i]].get_last_name()[0])
        print()
        print("Test2 child naming convention success.")
        
if __name__ == '__main__':

    unittest.main()