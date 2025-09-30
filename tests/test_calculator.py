from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 4), -3)
        self.assertEqual(subtract(10, 5), 5)
    def test_divide(self):
        self.asserEqual(divide(10, 2), 5)
        self.asserEqual(divide(-6, 3), -2)
        self.asserEqual(divide(4, 1), 4)
    if __name__ == '__main__':
        unittest.main()