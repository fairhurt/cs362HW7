
import unittest

from leap_year_hw7 import check_leap_year

class TestLeapYear(unittest.TestCase):
    def test1 (self):
        self.assertEqual(check_leap_year(2000), True)
    def test2 (self):
        self.assertEqual(check_leap_year(2020), True)
    def test3 (self):
        self.assertEqual(check_leap_year(2023), False)
   
    
        
  
if __name__ == '__main__':
    unittest.main(verbosity=2)