class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A or len(A) == 0:
            return 0
        end = 0
        i = 1
        while i < len(A):
            if A[i] != A[i - 1]:
                end += 1
                if end != i:
                    A[end] = A[i]
            i += 1
        return end + 1

    def removeDuplicatesRec(self, A, start, end):
        if A[start] == A[end]:
            return 1
        mid = (start + end) / 2
        dup = 1 if A[mid] == A[mid + 1] else 0
        return self.removeDuplicatesRec(A, start, mid) + \
               self.removeDuplicatesRec(A, mid + 1, end) - \
               dup


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(2, self.s.removeDuplicates([1, 1, 2]))
        self.assertEqual(3, self.s.removeDuplicates([1, 1, 1, 1, 1, 2, 3]))
        self.assertEqual(6, self.s.removeDuplicates([1, 1, 1, 1, 1, 2, 3,
                                                     4, 4, 4, 4, 4, 4, 4,
                                                     5, 6]))

if __name__ == '__main__':
    unittest.main()
