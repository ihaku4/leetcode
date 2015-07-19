class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        if len(nums) <= 2:
            return min(nums)

        numsH = nums[0]
        numsT = nums[-1]

        lo, hi = 0, len(nums) - 2
        while lo <= hi:
            m = (lo + hi) / 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            else:
                if nums[m] >= numsH:
                    lo = m + 1
                if nums[m] <= numsT:
                    hi = m - 1


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(0, self.s.findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(0, self.s.findMin([0]))
        self.assertEqual(0, self.s.findMin([1, 0]))
        self.assertEqual(0, self.s.findMin([0, 1]))
        self.assertEqual(0, self.s.findMin([0, 1, 3]))

if __name__ == '__main__':
    unittest.main()
