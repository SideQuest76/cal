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
    def test_caluc2(self):
        first2 = caluc.calculator(2, 9)
        second2 = caluc.calculator(7,1)
        third2 = caluc.calculator(12, 48)
        fouth2 = caluc.calculator(56, 54)

        self.assertEqual(first2.minus(),-7)
        self.assertEqual(second2.minus(),6)
        self.assertEqual(third2.minus(),-36)
        self.assertEqual(fouth2.minus(),2)
    def test_caluc_multiply(self):
        first3 = caluc.calculator(2, 9)
        second3 = caluc.calculator(7,1)
        third3 = caluc.calculator(12, 48)
        fouth3 = caluc.calculator(56, 54)

        self.assertEqual(first3.multiply(),18)
        self.assertEqual(second3.multiply(),7)
        self.assertEqual(third3.multiply(),576)
        self.assertEqual(fouth3.multiply(),3024)
    def test_caluc_division(self):
        first4 = caluc.calculator(15, 3)
        second4 = caluc.calculator(18,3)
        third4 = caluc.calculator(144, 12)
        fouth4 = caluc.calculator(20, 5)

        self.assertEqual(first4.division(),5)
        self.assertEqual(second4.division(),6)
        self.assertEqual(third4.division(),12)
        self.assertEqual(fouth4.division(),4)
if __name__ == "__main__":
    unittest.main()