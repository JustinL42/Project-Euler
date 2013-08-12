#!C:\Python33\python.exe
import unittest
twentysix = __import__('026')



class test_026(unittest.TestCase):

    def test_repeating_digits(self):
        d = twentysix.repeating_digits
        
        self.assertEqual(d(2), 0)
        self.assertEqual(d(3), 1)
        self.assertEqual(d(6), 1)
        self.assertEqual(d(7), 6)
        self.assertEqual(d(8), 0)
        self.assertEqual(d(499), 498)
        # self.assertEqual(d(2), 0)
        # self.assertEqual(d(2), 0)
        # self.assertEqual(d(2), 0)
        # self.assertEqual(d(2), 0)
        # self.assertEqual(d(2), 0)

if __name__ == '__main__':
    unittest.main()