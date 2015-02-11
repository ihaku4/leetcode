class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        end = 0
        i = 0
        while i < len(A):
            if A[i] != elem:
                if end != i:
                    A[end] = A[i]
                end += 1
            i += 1
        return end


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        A = [1, 2, 3, 4, 4, 5]
        self.assertEqual(4, self.s.removeElement(A, 4))
        self.assertEqual(A[:4], [1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
