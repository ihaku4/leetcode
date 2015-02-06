class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        div = 10
        while x / div > 0:
            div *= 10
        head_div = div
        tail_div = 10
        while head_div > tail_div:
            h = (x % head_div) / (head_div / 10)
            t = (x % tail_div) / (tail_div / 10)
            if h != t:
                return False
            head_div /= 10
            tail_div *= 10
        return True

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_normal(self):
        self.assertTrue(self.s.isPalindrome(12321))
        self.assertTrue(self.s.isPalindrome(52325))
        self.assertTrue(self.s.isPalindrome(111))
        self.assertTrue(self.s.isPalindrome(11))
        self.assertTrue(self.s.isPalindrome(1))
        self.assertTrue(self.s.isPalindrome(0))

        self.assertFalse(self.s.isPalindrome(-1))

unittest.main()
