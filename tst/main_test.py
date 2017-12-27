#Import testing suite & do the things
import unittest


#modify this base test case
class my_test(unittest.TestCase):
    def test(self):
        self.assertEqual(3, 3)
