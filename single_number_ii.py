class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        mark, twos = 0, 0
        for n in A:
            # if n < 0:
            #     n += 1 << 32
            twos ^= mark & n
            mark ^= n & ~(n & twos & mark)
        # if mark & 0x80000000:
        #     mark -= (1 << 32)
        return mark


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(2, self.s.singleNumber([1, 2, 3, 1, 3, 1, 3]))
        self.assertEqual(3, self.s.singleNumber([1, 2, 2, 1, 2, 1, 3]))
        self.assertEqual(-4, self.s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))

if __name__ == '__main__':
    unittest.main()
