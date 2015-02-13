class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda a, b: a ^ b, A)

    def _deprecated_singleNumber(self, A):
        s = sum(A)
        even = s % 2 == 0
        for n in A:
            if even:
                if n % 2 == 0:
                    if (s - len(A) - n + 1) % 2 == 0:
                        return n
                else:
                    if (s - n) % 2 == 0:
                        return n
            else:  # odd
                if n % 2 == 0:
                    if (s - len(A) - n + 1) % 2 == 1:
                        return n
                else:
                    if (s - n) % 2 == 1:
                        return n

    def __singleNumber(self, A):
        exist = {}
        for n in A:
            exist[n] = 2 if n in exist else 1
        for n in A:
            if exist[n] == 1:
                return n

    def _singleNumber(self, A):
        # mark = [0] * 0x100000000
        mark = [0] * 0x10000
        for n in A:
            mark[n] += 1
        for n in A:
            if mark[n] == 1:
                return n
        return None


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(5, self.s.singleNumber([1, 2, 3, 4, 2, 3, 1, 4, 5]))

if __name__ == '__main__':
    unittest.main()
