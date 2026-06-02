import unittest

# Function to test
def add(a, b):
    return a + b

# Test Framework
class TestAddition(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -4), -6)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

# Run tests automatically
if __name__ == "__main__":
    unittest.main()