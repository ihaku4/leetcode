class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        return self.helper(num, 0, len(num) - 1)

    def helper(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return start if num[start] > num[end] else end

        mid = (start + end) / 2
        if num[mid + 1] > num[mid]:
            return self.helper(num, mid + 1, end)
        elif num[mid + 1] < num[mid]:
            return self.helper(num, start, mid)
        return None  # input invalid

    def _helper(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return start if num[start] > num[end] else end

        mid = (start + end) / 2
        #  /   \
        # -1 m +1
        if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
            return mid
        # \    /
        # -1 m +1
        #      /
        #  /
        # -1 m +1
        elif num[mid + 1] > num[mid]:
            return self.helper(num, mid + 1, end)
        #  \
        #      \
        # -1 m +1
        elif num[mid - 1] > num[mid]:
            return self.helper(num, start, mid - 1)
        return None  # input invalid

    def _findPeakElement(self, num):
        if len(num) < 2:
            return 0
        if num[0] > num[1]:
            return 0
        if num[-1] > num[-2]:
            return len(num) - 1
        i = 1
        while i < len(num) - 1:
            if num[i] > num[i - 1] and num[i] > num[i + 1]:
                return i
            elif num[i] > [i + i]:
                i += 2
            else:
                i += 1
        return 0


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(2, self.s.findPeakElement([1, 2, 3, 1]))
        self.assertEqual(0, self.s.findPeakElement([2]))
        self.assertEqual(0, self.s.findPeakElement([3, 2]))
        self.assertEqual(1, self.s.findPeakElement([3, 4]))
        print self.s.findPeakElement([1, 2, 3, 1])

if __name__ == '__main__':
    unittest.main()
