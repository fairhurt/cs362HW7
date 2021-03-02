import unittest

from question1_code import print_multiples

class TestMultiples(unittest.TestCase):
      
    def test1(self):
        num=list(range(1,101))
        self.assertEqual(print_multiples(num), True)
        
      

        
  
if __name__ == '__main__':
   unittest.main(verbosity=2)
