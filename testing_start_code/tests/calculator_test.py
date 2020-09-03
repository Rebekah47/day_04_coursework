import unittest
from src.calculator import add, divide, multiply, subtract, add_3_num

class TestCalculator(unittest.TestCase):

# 1. Arrange
# 2. Act 
# 3. Assert 

    def test_add(self):
        self.assertEquals(5, add(2,3))
    
    def test_subtract(self):
        self.assertEquals(3, subtract(10,7))
    
    def test_multiply(self):
        self.assertEquals(30, multiply(6,5))
    
    def test_divide(self):
        self.assertEquals(6, divide(30, 5))
    
    def test_add_3_num(self):
        self.assertEquals(14, add_3_num(3,7,4))


pass