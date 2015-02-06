class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        if i < 0:
            return [1] + digits
        return digits

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_overflow(self):
        self.assertEqual([1] + [0]*4, self.s.plusOne([9]*4))

    def test_normal(self):
        self.assertEqual([1, 2, 3, 5], self.s.plusOne([1, 2, 3, 4]))
        self.assertEqual([1, 2, 4, 0], self.s.plusOne([1, 2, 3, 9]))
        self.assertEqual([2, 0, 0, 0], self.s.plusOne([1, 9, 9, 9]))

unittest.main()
