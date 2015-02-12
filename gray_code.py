class Solution:
    # @return a list of integers
    def grayCode(self, n):
        grayCode = [0]
        num = -1
        while num != grayCode[-1]:
            num = grayCode[-1]
            for i in range(n):
                s = 1 << i
                new = num ^ s
                if new not in grayCode:
                    grayCode.append(new)
                    break
        return grayCode


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def _test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual([0, 1, 3, 2], self.s.grayCode(2))
        n = 3
        for n in range(100):
            grayCode = self.s.grayCode(n)
            for i in range(n):
                self.assertTrue(i in grayCode)

    def test_large_case(self):
        for i in range(100):
            code = self.s.grayCode(i)
            print i, len(code)

if __name__ == '__main__':
    unittest.main()
