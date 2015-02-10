class Solution:

    # c should be upper case, before call
    def isAlpha(self, c):
        return c >= 'A' and c <= 'Z' or \
            c >= '0' and c <= '9'

    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.upper()
        head = 0
        tail = len(s) - 1
        while head < tail:
            if not self.isAlpha(s[head]):
                head += 1
                continue
            if not self.isAlpha(s[tail]):
                tail -= 1
                continue
            if s[head] != s[tail]:
                return False
            else:
                head += 1
                tail -= 1
        return True


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        return

    def test_normal(self):
        self.assertEqual(0, 0)
        self.assertTrue(self.s.isPalindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(self.s.isPalindrome('race a car'))
        self.assertFalse(self.s.isPalindrome('1a2'))

if __name__ == '__main__':
    unittest.main()
