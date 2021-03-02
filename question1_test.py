import unittest

from question1_code import print_multiples

class TestAverage(unittest.TestCase):
    def test1 (self):
        count = 0
        while count < 100:
            if(count %3 == 0 and count % 5 ==0):
                self.assertEqual(print_multiples(count),'FizzBuzz')
            elif(count % 3 == 0):
                self.assertEqual(print_multiples(count),'Fizz')
            elif(count % 5 ==0):
                self.assertEqual(print_multiples(count),'Buzz')
            else:
                self.assertEqual(print_multiples(count), count)
            count = count + 1
    
        
  
if __name__ == '__main__':
    unittest.main(verbosity=2)