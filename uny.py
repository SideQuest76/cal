import unittest
import caluc

class TestStringMethods(unittest.TestCase):
    def test_caluc(self):
        first = caluc.calculator(2, 9)
        second = caluc.calculator(7,1)
        third = caluc.calculator(12, 48)
        fouth = caluc.calculator(56, 54)

        self.assertEqual(first.plus(),11)
        self.assertEqual(second.plus(),8)
        self.assertEqual(third.plus(),60)
        self.assertEqual(fouth.plus(),110)

if __name__ == "__main__":
    unittest.main()